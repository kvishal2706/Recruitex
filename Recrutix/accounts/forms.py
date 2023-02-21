from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.forms import widgets
from .models import CustomUser
class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.',widget = forms.TextInput(attrs={'class':'username'}))
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'phone', 'first_name', 'last_name')
        widget = {
            'username': forms.TextInput(attrs={'class':'username'}),
            'email': forms.TextInput(attrs={'class':'email_name'}),
            'phome': forms.NumberInput(attrs={'class':'phome_name'}),
            'first_name': forms.TextInput(attrs={'class':'first_name'}),
            'last_name': forms.TextInput(attrs={'class':'last_name'})
        }

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone', 'first_name', 'last_name')
        widget = {
            'username': forms.TextInput(attrs={'class':'username_name'}),
            'email': forms.TextInput(attrs={'class':'email_name'}),
            'phome': forms.NumberInput(attrs={'class':'phome_name'}),
            'first_name': forms.TextInput(attrs={'class':'first_name'}),
            'last_name': forms.TextInput(attrs={'class':'last_name'})
        }
