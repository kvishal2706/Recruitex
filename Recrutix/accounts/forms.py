from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.forms import ModelForm
from .models import CustomUser, Feedback
from tinymce.widgets import TinyMCE

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
        
        
        
class loginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your Username/Email','class':'bg-red-200'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter your Password','class': 'bg-red-200'}))
    
class NewsletterForm(forms.Form):
    subject = forms.CharField()
    receivers = forms.CharField()
    message = forms.CharField(widget=TinyMCE(), label="Email content")
    
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder':'Name', 'class':'w-80 my-2 p-3 bg-[#111534] text-black focus:outline-none focus:bg-[#1E2A7B] text-white rounded-tr-2xl rounded-bl-2xl'})
        self.fields['email'].widget.attrs.update({'placeholder':'Enter your Email', 'class':'w-80 my-2 p-3 bg-[#111534] text-black focus:outline-none focus:bg-[#1E2A7B] text-white rounded-tr-2xl rounded-bl-2xl'})
        self.fields['feedback'].widget.attrs.update({'placeholder':'Please enter your Valuable Feedback', 'class':'w-80 my-2 p-3 h-32 bg-[#111534] text-black focus:outline-none focus:bg-[#1E2A7B] text-white rounded-tr-2xl rounded-bl-2xl'})
    
    
    