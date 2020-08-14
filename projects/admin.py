from django.contrib import admin

#   needed imports
from .models import Project, Technologie

# Register your models here.
admin.site.register(Project)
admin.site.register(Technologie)