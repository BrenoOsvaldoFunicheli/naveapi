from django.db import models

#   needed imports
from projects.models import Project
from django.contrib.auth.models import User
# Create your models here.


class JobRole(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Naver(models.Model):

    STATUS = (
        ('A', 'Actived'),
        ('D', 'Deleted')
    )

    name = models.CharField(max_length=100)
    job_role = models.ForeignKey(JobRole, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=1, choices=STATUS, default='A')
    admission_date = models.DateField(null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    projects = models.ManyToManyField(Project)
    creator = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    @property
    def job(self):
        # return str(self.pk)
        return str(self.job_role)#JobRole.objects.get(pk=self.job_role).name
