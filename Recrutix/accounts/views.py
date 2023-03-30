from .forms import CustomUserCreationForm,NewsletterForm
from .models import CustomUser, SubscribedUsers
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth import get_user_model
from django.views.generic import CreateView
from django.contrib.auth.decorators import user_passes_test
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.mail import EmailMessage
from django.contrib import messages
from django.conf import settings


def SignUpView(request):
    form = CustomUserCreationForm()
    print(form)
    if request.method=='POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')
            
    return render(request, 'registration/UserSignup.html',{
        'form': form
    })



def index(request):
    return render(request,'UserView/home.html') 

def about_us(request):
    return render(request, 'UserView/about_us.html')

def contact_us(request):
    return render(request, 'UserView/contact_us.html')


def profiles_list(request):
    profiles = CustomUser.objects.all()
    print(profiles)
    return render(request, 'UserView/profiles.html',{'profiles':profiles})

def subscribe(request):
    if request.method == 'POST':
        print("1111111")
        email = request.POST.get('email', None)
        if not email:
            print("2222222")
            messages.error(request,"You must enter valid email.")
            return redirect('/')
        if get_user_model().objects.filter(email=email).first():
            print("3333333")
            messages.error(request, f"FOund registered user with associsted {email} email.")
            return redirect(request.META.get("HTTP_REFERER",'/'))
        subscribe_users = SubscribedUsers.objects.filter(email=email).first()
        if subscribe_users:
            print("4444444")
            messages.error(request, f"{email} email address is already ")
            return redirect(request.META.get("HTTP_REFERER",'/'))
        try:
            print("5555555")
            validate_email(email)
        except ValidationError as e:
            print("6666666")
            messages.error(request, e.messages[0])
            return redirect('/')
        
        subscribe_model_instance = SubscribedUsers()
        subscribe_model_instance.email = email
        subscribe_model_instance.save()
        messages.success(request, f"{email} email was successfully subscrubed to our newsletters!")
        return redirect(request.META.get("HTTP_REFERER",'/'))
    
@user_passes_test(lambda u: u.is_superuser)
def newsletter(request):
    if request.method=='POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get('subject')
            receivers = form.cleaned_data.get('receivers').split(', ')
            email_message = form.cleaned_data.get('message')
            
            # mail = send_mail(subject,email_message, settings.EMAIL_HOST_USER, receivers, fail_silently=False)
            # mail2 = send_mail('Subject','body','raghavagatadi12@gmail.com',receivers, fail_silently=False)
            mail = EmailMessage(subject, email_message, 'raghavagatadi12@gmail.com', receivers, bcc=receivers)
            
            if mail.send():
                messages.success(request,"Email sent successfully.")
            else:
                messages.error(request, "There was error sending email")
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
        return redirect('/')
    
    form = NewsletterForm()
    form.fields['receivers'].initial = ','.join([active.email for active in SubscribedUsers.objects.all()])
    return render(request, 'UserView/newsletter.html', {'form':form})