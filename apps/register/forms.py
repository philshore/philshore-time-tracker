from django import forms
from django.contrib.auth.models import User
from apps.register.models import UserComponent


class RegistrationUserForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(label=("Password"),
                               widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'first_name',
                  'last_name', 'email', 'password')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'password': forms.TextInput(attrs={'placeholder': 'Password'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email@gmail.com'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
        }


class RegistrationUserComponentForm(forms.ModelForm):

    class Meta:
        model = UserComponent
        fields = ('component',)
        widgets = {
            'component': forms.TextInput(attrs={'placeholder': 'Component'}),
        }
