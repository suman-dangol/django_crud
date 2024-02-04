from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput


# Django ko userCreatedForm bata user create garne inherit garne

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1' , 'password2']
    
#Authentication django le dinxa
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())