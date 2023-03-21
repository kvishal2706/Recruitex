from django.forms import ModelForm
from .models import ApplicationForm

class ApplicationForm(ModelForm):
    # first_name = forms.CharField(max_length=30, required=True, help_text='Required.',widget=forms.TextInput(attrs={'placeholder': 'First Name','class':'input'}))
    # last_name = forms.CharField(max_length=30, required=True, help_text='Required.',widget=forms.TextInput(attrs={'placeholder': 'Last Name','class':'input'}))
    # email = forms.EmailField(required=True, help_text="Required",widget=forms.TextInput(attrs={'placeholder': 'Email','class':'input'}))
    # about_you = forms.CharField(required=False, help_text= 'Write a short description about you.', widget=forms.Textarea(attrs={'placeholder': 'Tell us a little about you.','class':'input'}))
    # why_you = forms.CharField(required=True, help_text= 'Write a short description why we should we take you.', widget=forms.Textarea(attrs={'placeholder': 'What makes you right for us?','class':'input'}))
    
    class Meta:
        model = ApplicationForm
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'placeholder':'First name','class': 'input'})
        self.fields['last_name'].widget.attrs.update({'placeholder':'Last Name','class': 'input'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email','class':'input'})
        self.fields['about_you'].widget.attrs.update({'placeholder': 'Tell us a little about you.','class':'input'})
        self.fields['why_you'].widget.attrs.update({'placeholder': 'What makes you right for us?','class':'input'})