from django.contrib import admin

#  needed imports 
from .models import Naver, JobRole

#   Register your models here.
admin.site.register(Naver)
admin.site.register(JobRole)