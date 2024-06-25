from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from users.models import User

class UserLoginForm(AuthenticationForm):
    pass
    class Meta:
        model = User
        fields = ['username', 'password',]


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            "username",
            "phone_number",
            "password1",
            "password2",
        )
    
    username = forms.CharField()
    phone_number = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()