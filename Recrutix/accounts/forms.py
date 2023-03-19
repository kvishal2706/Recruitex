from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.forms import widgets
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.',widget=forms.TextInput(attrs={'placeholder': 'First Name','class':'input'}))
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.',widget=forms.TextInput(attrs={'placeholder': 'Last Name','class':'input'}))
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.',widget=forms.TextInput(attrs={'placeholder': 'example@gmail.com','class':'input'}))
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'phone', 'first_name', 'last_name','password1','password2')
        widgets = {
            'phone': forms.TextInput(attrs={'placeholder': '+91 ##########','class':'input'}),
            'username': forms.TextInput(attrs={'placeholder': 'Username','class':'input'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'placeholder':'Enter your Password','class': ''})
        self.fields['password2'].widget.attrs.update({'placeholder':'Confirm your Password','class': ''})
        
class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone', 'first_name', 'last_name')
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'border-2','placeholder':"Username"}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class':'border-2','placeholder':"Password"}))