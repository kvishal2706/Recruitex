from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.forms import widgets
from .models import CustomUser
class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.',widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.',widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.',widget=forms.TextInput(attrs={'placeholder': 'example@gmail.com'}))
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'phone', 'first_name', 'last_name','password1','password2')
        widgets = {
            'phone': forms.TextInput(attrs={'placeholder': '+91 ##########'}),
            'username': forms.TextInput(attrs={'placeholder': 'Username'})
        }
        
class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone', 'first_name', 'last_name')
        
