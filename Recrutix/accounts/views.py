from .forms import CustomUserCreationForm,NewsletterForm,UpdateInformationForm,addQualificationsForm,addWorkExperienceForm,SkillsForm
from django.contrib.auth.decorators import login_required
from .models import CustomUser, SubscribedUsers, Qualification,WorkandExperience
from Jobs.models import Jobs
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import get_user_model
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
            messages.success(request,"Signup Successful. Please Login")
            return redirect('home-page')
            
    return render(request, 'registration/UserSignup.html',{
        'form': form
    })

@login_required
def update_information(request):
    User = request.user
    post_data = request.POST or None
    file_data = request.FILES or None
    form = UpdateInformationForm(instance = User)
    
    if request.method=='POST':
        form = UpdateInformationForm(post_data,file_data, instance = User)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('profile-page',slug=request.user.slug)
    
    return render(request,'registration/update_information.html',{
        'form':form
    })

@login_required
def add_qualifications(request):
    User = request.user
    form = addQualificationsForm()
    if request.method=='POST':
        form = addQualificationsForm(request.POST)
        if form.is_valid():
            my_model = form.save()
            qualification = Qualification.objects.get(id=my_model.id)
            User.qualifications.add(qualification)
            messages.success(request,"your Qualification added successfully.")
            return redirect('add-qualification')
    return render(request,'registration/add_qualification.html',{
        'form':form
    })
@login_required
def add_workExperience(request):
    User = request.user
    form = addWorkExperienceForm()
    if request.method=='POST':
        form = addWorkExperienceForm(request.POST)
        if form.is_valid():
            my_model = form.save()
            work_experience = WorkandExperience.objects.get(id=my_model.id)
            User.work_experience.add(work_experience)
            messages.success(request,"your Wok experience added successfully.")
            return redirect('add-workExperience')
    return render(request,'registration/add_workexperience.html',{
        'form':form
    })

def add_skills(request):
    User = request.user
    form = SkillsForm(instance=User)
    if request.method=='POST':
        form = SkillsForm(request.POST,instance=User)
        if form.is_valid():
            form.save()
            return redirect('profile-page', slug = request.user.slug)
    return render(request,'registration/add_skills.html',{
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
    uploaded_jobs = Jobs.objects.filter(recruiter = request.user)
    return render(request,'UserView/profile_page.html', {
        'my': user,
        'jobs':uploaded_jobs
        })



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
    