from django.shortcuts import get_object_or_404, redirect, render
from .models import Jobs
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import ApplicationForm

from django.contrib.auth.mixins import (
LoginRequiredMixin,
UserPassesTestMixin # new
)

class JobsListView(LoginRequiredMixin, ListView):
    model=Jobs
    template_name="jobs_list.html"
    context_object_name="jobss"

def JobsDetailView(request, slug):  # new
    model = get_object_or_404(Jobs, slug=slug)
    form = ApplicationForm()
    if request.method =='POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jobs_list')
    # template_name = 'Jobs/jobs_detail.html'
    return render(request, 'Jobs/jobs_detail.html', {
        'form': form,
        'object':model
    })
    

def UpdateJob(request, slug):
    return render(request, 'Jobs/jobs_edit.html')

def DeleteJob(request, slug):
    return render(request, 'Jobs/jobs_delete.html')


class JobsCreateView(LoginRequiredMixin, CreateView): # new
    model = Jobs
    template_name = 'Jobs/jobs_new.html'
    fields = ('title', 'Designation','location','salary','about_job','about_company','workings')

    def form_valid(self, form): # new
        form.instance.recruiter = self.request.user
        return super().form_valid(form)
