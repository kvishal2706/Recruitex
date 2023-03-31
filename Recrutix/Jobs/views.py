from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Jobs,Tag,Jobs_type
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import ApplicationForm
from.filters import JobFilter
from django.db.models import Q
from accounts.models import CustomUser

from django.contrib.auth.mixins import (
LoginRequiredMixin,
UserPassesTestMixin # new
)


def JobsListView(request):
    job_filter = JobFilter(request.GET, queryset = Jobs.objects.all())
    jobs = Jobs.objects.all()
    if 'q' in request.GET:
        query = request.GET['q']
        multiple_query = Q(Q(title__icontains=query) | Q(designation__icontains=query)| Q(location__icontains=query))
        jobs = Jobs.objects.filter(multiple_query)
    elif job_filter:
        jobs = job_filter.qs
    else:
        jobs = Jobs.objects.all()
    return render(request, "Jobs/jobs_list.html",{
        'jobs': jobs,
        'form': job_filter.form
    })
    

@login_required
def JobsDetailView(request, slug):  # new
    model = get_object_or_404(Jobs, slug=slug)
    # print(model)
    form = ApplicationForm()
    if request.method =='POST':
        form = ApplicationForm(request.POST)

        if form.is_valid():
            ferm = form.save(commit=False)
            model.job_applied_users.add(request.user)
            ferm.job = model
            request.user.applied_jobs.add(model)
            print(ferm.job)
            ferm.save()
            return redirect('jobs_list')
        
    # template_name = 'Jobs/jobs_detail.html'
    return render(request, 'Jobs/jobs_detail.html', {
        'form': form,
        'object':model
    })
    

@login_required
def UpdateJob(request, slug):
    return render(request, 'Jobs/jobs_edit.html')

@login_required
def DeleteJob(request, slug):
    return render(request, 'Jobs/jobs_delete.html')


class JobsCreateView(LoginRequiredMixin, CreateView): # new
    model = Jobs
    template_name = 'Jobs/jobs_new.html'
    fields = ('title', 'Designation','location','salary','about_job','about_company','workings')

    def form_valid(self, form): # new
        form.instance.recruiter = self.request.user
        return super().form_valid(form)

