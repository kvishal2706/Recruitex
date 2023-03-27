from django.shortcuts import get_object_or_404, redirect, render
from .models import Jobs,Tag,Job_Duration_type,Jobs_type
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import ApplicationForm
from.filters import JobFilter

from django.contrib.auth.mixins import (
LoginRequiredMixin,
UserPassesTestMixin # new
)

def JobsListView(request):
    job_filter = JobFilter(request.GET, queryset = Jobs.objects.all())
    return render(request, "Jobs/jobs_list.html",{
        'jobs': job_filter.qs,
        'form': job_filter.form
    })

def JobsDetailView(request, slug):  # new
    model = get_object_or_404(Jobs, slug=slug)
    job = Jobs.objects.filter(slug=slug)
    form = ApplicationForm()
    if request.method =='POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            # user.applied_jobs = Jobs.objects.filter(slug=slug)
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

