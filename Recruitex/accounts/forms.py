from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.forms import ModelForm
from .models import CustomUser, Feedback, Qualification, WorkandExperience,Skills
from tinymce.widgets import TinyMCE


class DateInput(forms.DateInput):
    input_type = 'date'

class SkillsForm(forms.ModelForm):
    skills_tag = forms.ModelMultipleChoiceField(queryset=Skills.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={'class':''}))
    class Meta:
        model = CustomUser
        fields = ('skills_tag',)
    
    

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.',widget=forms.TextInput(attrs={'placeholder': 'First Name','class':'text-base w-11/12  focus:border-2 focus:border-[#18d85b]'}))
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.',widget=forms.TextInput(attrs={'placeholder': 'Last Name','class':'text-base w-11/12 focus:border-2 focus:border-[#18d85b]'}))
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.',widget=forms.TextInput(attrs={'placeholder': 'example@gmail.com','class':'text-base w-full focus:border-2 focus:border-[#18d85b]'}))
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('first_name', 'username', 'email', 'phone', 'last_name','password1','password2')
        widgets = {
            'phone': forms.TextInput(attrs={'placeholder': '+91 ##########','class':'text-base  w-full focus:border-2 focus:border-[#18d85b]'}),
            'username': forms.TextInput(attrs={'placeholder': 'Username','class':'text-base w-full focus:border-2 focus:border-[#18d85b]'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'placeholder':'Enter your Password','class': 'text-base w-full focus:border-2 focus:border-[#18d85b]'})
        self.fields['password2'].widget.attrs.update({'placeholder':'Confirm your Password','class': 'text-base w-full focus:border-2 focus:border-[#18d85b]'})
        
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
        exclude = ('created_date',)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder':'Name', 'class':'w-80 my-2 p-3 bg-[#111534] text-black focus:outline-none focus:bg-[#1E2A7B] text-white rounded-tr-2xl rounded-bl-2xl border-e-2 border-s-2 border-[#0089A5]'})
        self.fields['email'].widget.attrs.update({'placeholder':'Enter your Email', 'class':'w-80 my-2 p-3 bg-[#111534] text-black focus:outline-none focus:bg-[#1E2A7B] text-white rounded-tr-2xl rounded-bl-2xl border-e-2 border-s-2 border-[#0089A5]'})
        self.fields['feedback'].widget.attrs.update({'placeholder':'Please enter your Valuable Feedback', 'class':'w-80 my-2 p-3 h-32 bg-[#111534] text-black focus:outline-none focus:bg-[#1E2A7B] text-white rounded-tr-2xl rounded-bl-2xl border-e-2 border-s-2 border-[#0089A5]'})
    
    
    
    
class UpdateInformationForm(forms.ModelForm):
    dob = forms.DateField(widget=DateInput)
    class Meta:
        model = CustomUser
        fields = '__all__'
        exclude = ('password','last_login','groups','user_permissions','date_joined','is_staff','is_superuser','is_active','skills_tag','projects','applied_jobs','qualifications','work_experience','awards','slug','is_recruiter',)
        
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class':'w-[14rem] px-4 py-2 focus:outline-none border-0 rounded-lg'})
        self.fields['last_name'].widget.attrs.update({'class':'w-[14rem] px-4 py-2 focus:outline-none border-0 rounded-lg'})
        self.fields['email'].widget.attrs.update({'class':'w-[14rem] px-4 py-2 focus:outline-none border-0 rounded-lg'})
        self.fields['username'].widget.attrs.update({'class':'w-[14rem] px-4 py-2 focus:outline-none border-0 rounded-lg'})
        self.fields['phone'].widget.attrs.update({'class':'w-[14rem] px-4 py-2 focus:outline-none border-0 rounded-lg'})
        self.fields['gender'].widget.attrs.update({'class':'w-[14rem] px-4 py-2 focus:outline-none border-0 rounded-lg'})
        self.fields['profile_photo'].widget.attrs.update({'class':'w-[15rem] px-4 py-2 focus:outline-none border-0'})
        self.fields['dob'].widget.attrs.update({'placeholder':'YYYY-MM-DD','class':'min-w-[14rem] px-4 py-2 focus:outline-none border-0 rounded-lg'})
        self.fields['age'].widget.attrs.update({'placeholder':'Eg: 18','class':'min-w-[12rem] ml-8 px-4 py-2 focus:outline-none border-0 rounded-lg'})
        self.fields['salary'].widget.attrs.update({'placeholder':'','class':'min-w-[14rem] px-4 py-2 focus:outline-none border-0 rounded-lg'})
        self.fields['address'].widget.attrs.update({'placeholder':'','class':'min-w-[12rem] px-4 py-2 focus:outline-none border-0 rounded-lg'})
        self.fields['qualification'].widget.attrs.update({'placeholder':'','class':'min-w-[14rem] px-4 py-2 focus:outline-none border-0 rounded-lg'})
        self.fields['major_skill'].widget.attrs.update({'placeholder':'','class':'min-w-[16rem] px-4 py-2 focus:outline-none border-0 rounded-lg'})
        self.fields['about_me'].widget.attrs.update({'placeholder':'Write a short description about you','class':'h-20 w-full border-0 rounded-lg p-2 mt-2'})
        self.fields['languages'].widget.attrs.update({'placeholder':'','class':'w-[12rem] px-4 py-2 focus:outline-none border-0 rounded-lg'})
        self.fields['interests'].widget.attrs.update({'placeholder':'','class':'min-w-[16rem] px-4 py-2 focus:outline-none border-0 rounded-lg'})
        self.fields['facebook_link'].widget.attrs.update({'placeholder':'','class':'w-[12rem] px-4 py-2 focus:outline-none border-0 rounded-lg'})
        self.fields['twitter_link'].widget.attrs.update({'placeholder':'','class':'min-w-[16rem] px-4 py-2 focus:outline-none border-0 rounded-lg'})
        self.fields['instagram_link'].widget.attrs.update({'placeholder':'','class':'w-[12rem] px-4 py-2 focus:outline-none border-0 rounded-lg'})
        self.fields['linkedin_link'].widget.attrs.update({'placeholder':'','class':'min-w-[16rem] px-4 py-2 focus:outline-none border-0 rounded-lg'})
        
class addQualificationsForm(forms.ModelForm):
    class Meta:
        model = Qualification
        fields = '__all__'
        
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['institute_name'].widget.attrs.update({'placeholder':'Name of Institute','class':'border-2 border-[#9ea79d] rounded-xl focus:outline-none '})
        self.fields['degree_type'].widget.attrs.update({'placeholder':'Ex: B.tech, M.tech','class':'border-2 border-[#9ea79d] rounded-xl focus:outline-none '})
        self.fields['field_of_study'].widget.attrs.update({'placeholder':'Ex: CSE','class':'border-2 border-[#9ea79d] rounded-xl focus:outline-none text-gray-400'})
        self.fields['start_year'].widget.attrs.update({'placeholder':'Ex: 2021','class':'border-2 border-[#9ea79d] rounded-xl focus:outline-none text-gray-400'})
        self.fields['end_year'].widget.attrs.update({'placeholder':'Ex:2025','class':'border-2 border-[#9ea79d] rounded-xl focus:outline-none text-gray-400'})
        
class addWorkExperienceForm(forms.ModelForm):
    joining_date = forms.DateField(widget = DateInput)
    leaving_date = forms.DateField(widget = DateInput, required=False)
    class Meta:
        model = WorkandExperience
        fields = '__all__'        
        
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['job_title'].widget.attrs.update({'placeholder':'Work Position','class':'border-2 border-[#9ea79d] rounded-xl focus:outline-none '})
        self.fields['company_name'].widget.attrs.update({'placeholder':'Ex: Google','class':'border-2 border-[#9ea79d] rounded-xl focus:outline-none '})
        self.fields['joining_date'].widget.attrs.update({'placeholder':'','class':'border-2 border-[#9ea79d] rounded-xl focus:outline-none text-gray-400'})
        self.fields['leaving_date'].widget.attrs.update({'placeholder':'','class':'border-2 border-[#9ea79d] rounded-xl focus:outline-none text-gray-400'})
        self.fields['experience_description'].widget.attrs.update({'placeholder':'Write a short description about your work experience','class':'border-2 border-[#9ea79d] rounded-xl focus:outline-none text-gray-400 p-2 h-20'})
