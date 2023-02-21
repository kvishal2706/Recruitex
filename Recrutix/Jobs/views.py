from .models import Jobs
from django.views.generic import ListView,DetailView
from django.views.generic.edit import DeleteView,UpdateView,CreateView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import (
LoginRequiredMixin,
UserPassesTestMixin # new
)

class JobsListView(LoginRequiredMixin, ListView):
    model=Jobs
    template_name="jobs_list.html"
    context_object_name="jobss"

class JobsDetailView(LoginRequiredMixin, DetailView):  # new
    model = Jobs
    template_name = 'jobs_detail.html'

class JobsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): # new
    model = Jobs
    fields = ('title', 'Designation','location','salary','about_job','about_company','workings')
    template_name = 'jobs_edit.html'

    def test_func(self): # new
        obj = self.get_object()
        return obj.recruiter == self.request.user

class JobsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): # new
    model = Jobs
    template_name = 'jobs_delete.html'
    success_url = reverse_lazy('jobs_list')

    def test_func(self): # new
        obj = self.get_object()
        return obj.recruiter == self.request.user


class JobsCreateView(LoginRequiredMixin, CreateView): # new
    model = Jobs
    template_name = 'jobs_new.html'
    fields = ('title', 'Designation','location','salary','about_job','about_company','workings')

    def form_valid(self, form): # new
        form.instance.recruiter = self.request.user
        return super().form_valid(form)
