from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import EmailInput, TextInput


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ["email", "first_name", "last_name"]
        widgets = {
            'email': EmailInput(attrs={'class': 'form-control'}),
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
        }
