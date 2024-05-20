from django.contrib.auth import authenticate, get_user_model, login, logout
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, RedirectView

from main.forms import UserRegistrationForm
from main.services.emails import send_registration_email
from main.utils.token_generator import TokenGenerator


def index(request):
    return render(request, 'index.html')


def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:index')
    return render(request, 'registration/login.html')


def user_logout(request):
    logout(request)
    return redirect(reverse_lazy('main:index'))


class UserRegistrationView(CreateView):
    template_name = "registration/registration.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("main:index")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        send_registration_email(user_instance=user, request=self.request)
        return super().form_valid(form)


class UserActivationView(RedirectView):
    url = reverse_lazy("main:index")

    def get(self, request, pk, token, *args, **kwargs):
        try:
            current_user = get_user_model().objects.get(pk=pk)
        except (get_user_model().DoesNotExist, ValueError, TypeError):
            return HttpResponse("Activation failed 1.")

        if current_user and TokenGenerator().check_token(current_user, token):
            current_user.is_active = True
            current_user.save()
            login(request, current_user)
            return super().get(request, *args, **kwargs)
        return HttpResponse("Activation failed 2.")
