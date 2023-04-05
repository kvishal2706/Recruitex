from django.contrib import admin
from .models import Jobs,Tag,ApplicationForm,Job_Duration,Jobs_type

class JobsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}
    list_display = ['title','date','designation','location']

admin.site.register(Jobs,JobsAdmin)
admin.site.register(Tag)
admin.site.register(Jobs_type)
admin.site.register(Job_Duration)
admin.site.register(ApplicationForm)
