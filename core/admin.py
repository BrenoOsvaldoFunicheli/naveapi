from django.contrib import admin

#  needed imports 
from .models import Naver, JobRole, Project, Technologie

# Register your models here.
admin.site.register(Project)
admin.site.register(Technologie)
admin.site.register(Naver)
admin.site.register(JobRole)