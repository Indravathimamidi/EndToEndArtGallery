from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
        

from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=254, widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput)