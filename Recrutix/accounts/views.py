from .forms import CustomUserCreationForm,NewsletterForm,UserSignupForm_2
from django.contrib.auth.decorators import login_required
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
from django.db.models import Q
from .forms import FeedbackForm
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound


def SignUpView(request):
    form = CustomUserCreationForm()

    if request.method=='POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signup-2')
            
    return render(request, 'registration/UserSignup.html',{
        'form': form
    })

def Signup_page2(request):
    form = UserSignupForm_2()
    
    if request.method =='POST':
        form = UserSignupForm_2(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')
    return render(request,'registration/signUpPage_2.html',{
        'form':form
        })

def index(request):
    return render(request,'UserView/home.html') 

def about_us(request):
    return render(request, 'UserView/about_us.html')

def contact_us(request):
    form = FeedbackForm()
    if request.method =='POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for your feedback.")
            return redirect('home-page')
    return render(request, 'UserView/contact_us.html', {'form': form})

@login_required
def profile_page(request, slug):
    user = CustomUser.objects.filter(slug=slug)
    return render(request,'UserView/profile_page.html', {'my': user})



def profiles_list(request):
    profiles = CustomUser.objects.all()

    if 'q' in request.GET:
        query=request.GET['q']
        profiles=CustomUser.objects.filter(username__icontains=query)
    # print(profiles)
    return render(request, 'UserView/profiles.html',{'profiles':profiles})

def subscribe(request):

    if request.method == 'POST':
        email = request.POST.get('email', None)

        if not email:
            messages.error(request,"You must enter valid email.")
            return redirect('/')
        
        if get_user_model().objects.filter(email=email).first():
            messages.error(request, f"FOund registered user with associsted {email} email.")
            return redirect(request.META.get("HTTP_REFERER",'/'))

        subscribe_users = SubscribedUsers.objects.filter(email=email).first()

        if subscribe_users:
            messages.error(request, f"{email} email address is already ")
            return redirect(request.META.get("HTTP_REFERER",'/'))
        
        try:
            validate_email(email)

        except ValidationError as e:
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
            mail = EmailMessage(subject, email_message, f'Recrutix {request.user.email}', receivers, bcc=receivers)
            mail.content_subtype='html'

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


def cv_view(request, slug):
    fs = FileSystemStorage()
    profile = CustomUser.objects.get(slug = slug)
    file_path = str(profile.cv.path)
    if fs.exists(file_path):
        with fs.open(file_path) as pdf:
            response = HttpResponse(pdf, content_type="application/pdf")
            response['content-Disposition'] = f'inline; filename = {profile.cv.path}'
            return response
    else:
        HttpResponseNotFound("The requested file not found")
        
def resume_view(request, slug):
    fs = FileSystemStorage()
    profile = CustomUser.objects.get(slug = slug)
    file_path = str(profile.resume.path)
    if fs.exists(file_path):
        with fs.open(file_path) as pdf:
            response = HttpResponse(pdf, content_type="application/pdf")
            response['content-Disposition'] = f'inline; filename = {profile.resume.path}'
            return response
    else:
        HttpResponseNotFound("The requested file not found")
    