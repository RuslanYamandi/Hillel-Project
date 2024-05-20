from django.urls import path

from main.views import (UserActivationView, UserRegistrationView, index,
                        user_login, user_logout)

app_name = 'main'


urlpatterns = [
    path("", index, name="index"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("register/", UserRegistrationView.as_view(), name="register"),
    path("activate/<int:pk>/<str:token>/", UserActivationView.as_view(), name="activate"),
]
