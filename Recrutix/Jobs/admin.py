from django.contrib import admin
from .models import Jobs

# class JobsAdmin(admin.ModelAdmin):
    # prepopulated_fields = {"slug":("title",)}

# admin.site.register(Jobs,JobsAdmin)
admin.site.register(Jobs)
