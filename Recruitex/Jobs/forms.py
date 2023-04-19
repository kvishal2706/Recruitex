from django.forms import ModelForm
from django import forms
from .models import ApplicationForm
from .models import Jobs

class JobsCreationForm(forms.ModelForm):
    class Meta:
        model = Jobs
        fields = '__all__'
        exclude = ('date','recruiter','slug','job_applied_users',)
        
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'placeholder':'Company name','class':'border-2 border-[#9ea79d] rounded-xl focus:outline-none '})
        self.fields['designation'].widget.attrs.update({'placeholder':'Position name, M.tech','class':'border-2 border-[#9ea79d] rounded-xl focus:outline-none '})
        self.fields['location'].widget.attrs.update({'placeholder':'Ex: India','class':'border-2 border-[#9ea79d] rounded-xl focus:outline-none text-gray-400'})
        self.fields['salary'].widget.attrs.update({'placeholder':'Ex: 50k-75k','class':'border-2 border-[#9ea79d] rounded-xl focus:outline-none text-gray-400'})
        self.fields['type'].widget.attrs.update({'placeholder':'','class':' px-3 py-1 border-2 border-[#9ea79d] rounded-xl focus:outline-none text-gray-400'})
        self.fields['logo'].widget.attrs.update({'placeholder':'','class':' px-3 py-1 border-2 border-[#9ea79d] rounded-xl focus:outline-none '})
        self.fields['job_Category'].widget.attrs.update({'placeholder':'','class':' px-3 py-1 w-60 border-2 border-[#9ea79d] rounded-xl focus:outline-none '})
        self.fields['job_duration_type'].widget.attrs.update({'placeholder':'','class':' px-3 py-1 w-60 border-2 border-[#9ea79d] rounded-xl focus:outline-none text-gray-400'})
        self.fields['about_job'].widget.attrs.update({'placeholder':'Write a short description about your job','class':'border-2 border-[#9ea79d] rounded-xl focus:outline-none text-gray-400 p-2 h-20'})
        self.fields['about_company'].widget.attrs.update({'placeholder':'Write a short description about your company','class':'border-2 border-[#9ea79d] rounded-xl focus:outline-none text-gray-400 p-2 h-20'})
        self.fields['workings'].widget.attrs.update({'placeholder':'Write a short description about working at company','class':'border-2 border-[#9ea79d] rounded-xl focus:outline-none text-gray-400 p-2 h-20'})
        self.fields['skills_required'].widget.attrs.update({'placeholder':'Ex: B.tech, M.tech','class':'border-2 border-[#9ea79d] rounded-xl focus:outline-none '})
        self.fields['no_of_openings'].widget.attrs.update({'placeholder':'Ex: CSE','class':'border-2 border-[#9ea79d] rounded-xl focus:outline-none text-gray-400'})
        self.fields['embedded_location_url'].widget.attrs.update({'placeholder':'paste the src of your location from google maps.','class':'border-2 border-[#9ea79d] rounded-xl focus:outline-none text-gray-400 p-2 h-20'})
        


class ApplicationForm(ModelForm):
    # first_name = forms.CharField(max_length=30, required=True, help_text='Required.',widget=forms.TextInput(attrs={'placeholder': 'First Name','class':'input'}))
    # last_name = forms.CharField(max_length=30, required=True, help_text='Required.',widget=forms.TextInput(attrs={'placeholder': 'Last Name','class':'input'}))
    # email = forms.EmailField(required=True, help_text="Required",widget=forms.TextInput(attrs={'placeholder': 'Email','class':'input'}))
    # about_you = forms.CharField(required=False, help_text= 'Write a short description about you.', widget=forms.Textarea(attrs={'placeholder': 'Tell us a little about you.','class':'input'}))
    # why_you = forms.CharField(required=True, help_text= 'Write a short description why we should we take you.', widget=forms.Textarea(attrs={'placeholder': 'What makes you right for us?','class':'input'}))
    
    class Meta:
        model = ApplicationForm
        fields = '__all__'
        exclude = ('job',)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'placeholder':'First name','class': 'border border-gray-300 w-full text-black m-2 px-4 py-2'})
        self.fields['last_name'].widget.attrs.update({'placeholder':'Last Name','class': 'border border-gray-300 w-full m-2 m-2 px-4 py-2'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email','class':'border border-gray-300 w-full m-2 m-2 px-4 py-2'})
        self.fields['resume'].widget.attrs.update({'class':'border border-gray-300 w-full m-2 m-2 px-4 py-2'})
        self.fields['about_you'].widget.attrs.update({'placeholder': 'Tell us a little about you.','class':'border border-gray-300 w-full m-2 m-2 px-4 py-2 h-40'})
        self.fields['why_you'].widget.attrs.update({'placeholder': 'What makes you right for us?','class':'border border-gray-300 w-full m-2 m-2 px-4 py-2 h-40'})
        
class JobFilterForm(ModelForm):
    class Meta:
        model = Jobs
        fields = ['job_Category','type','job_duration_type']
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['job_Category'].widget.attrs.update({'class':'px-2 py-1 w-full border-gray-200 border-2 ml-4  cursor-pointer'})
        self.fields['type'].widget.attrs.update({'class':'px-2 py-1 w-full border-gray-200 border-2 ml-4 cursor-pointer'})
        self.fields['job_duration_type'].widget.attrs.update({'class':'px-2 py-1 w-full border-gray-200 border-2 ml-4 cursor-pointer'})