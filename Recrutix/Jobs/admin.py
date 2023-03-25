from django.contrib import admin
from .models import Jobs,Tag,ApplicationForm,Job_Duration_type,Jobs_type

class JobsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}

admin.site.register(Jobs,JobsAdmin)
admin.site.register(Tag)
admin.site.register(Jobs_type)
admin.site.register(Job_Duration_type)
admin.site.register(ApplicationForm)
