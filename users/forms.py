from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

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


class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "phone_number",
            "town",
            "street",
            "house",)

    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    phone_number = forms.CharField()
    town = forms.CharField()
    street = forms.CharField()
    house = forms.CharField()
