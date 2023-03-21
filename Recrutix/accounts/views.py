from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm


def SignUpView(request):
    form = CustomUserCreationForm()
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

