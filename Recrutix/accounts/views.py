from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm


def SignUpView(request):
    form = CustomUserCreationForm()
    if request.method=='POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            print("1")
            print("1")
            print("1")
            print("1")
            print("1")
            print("1")
            print("1")
            print("1")
            print("1")
            form.save()
            return redirect('home-page')
        else:
            print("2")
            print("2")
            print("2")
            print("2")
            print("2")
            print("2")
            print("2")
            print("2")
            print("2")
            
    return render(request, 'registration/UserSignup.html',{
        'form': form
    })

def index(request):
    return render(request,'UserView/home.html')

