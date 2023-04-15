import django_filters
from .models import Jobs
from .forms import JobFilterForm

class JobFilter(django_filters.FilterSet):
    class Meta:
        model = Jobs
        form = JobFilterForm
        fields = {
            'job_Category':['exact'],
            'type': ['exact'],
            'job_duration_type':['exact']
            }
   