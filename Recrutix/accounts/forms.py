from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.forms import widgets
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.',widget=forms.TextInput(attrs={'placeholder': 'First Name','class':'text-base w-11/12  focus:border-2 focus:border-purple-400'}))
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.',widget=forms.TextInput(attrs={'placeholder': 'Last Name','class':'text-base w-11/12 focus:border-2 focus:border-purple-400'}))
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.',widget=forms.TextInput(attrs={'placeholder': 'example@gmail.com','class':'text-base w-full focus:border-2 focus:border-purple-400'}))
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('first_name', 'username', 'email', 'phone', 'last_name','password1','password2','profile_photo')
        widgets = {
            'phone': forms.TextInput(attrs={'placeholder': '+91 ##########','class':'text-base  w-full focus:border-2 focus:border-purple-400'}),
            'username': forms.TextInput(attrs={'placeholder': 'Username','class':'text-base w-full focus:border-2 focus:border-purple-400'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'placeholder':'Enter your Password','class': 'text-base w-full focus:border-2 focus:border-purple-400'})
        self.fields['password2'].widget.attrs.update({'placeholder':'Confirm your Password','class': 'text-base w-full focus:border-2 focus:border-purple-400'})
        
class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('first_name', 'username', 'email', 'phone', 'last_name')
        
        # text-base h-6 py-3 px-8 w-72 rounded-3xl bg-white 