from django.db import models

#   needed imports
from projects.models import Project
# Create your models here.


class Naver(models.Model):
    JOB_ROLES = (
        ('dev', 'Desenvolvedor'),
        ('dba', 'Adminstrdor de Banco de Dados'),
        ('fte', 'Desenvolvedor Front-End')
    )

    STATUS = (
        ('A', 'Actived'),
        ('D', 'Deleted')
    )
    name = models.CharField(max_length=100)
    job_role = models.CharField(max_length=3, choices=JOB_ROLES, default='A')
    status = models.CharField(max_length=1, choices=STATUS, default='dev')
    admission_date = models.DateField(null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    projects = models.ManyToManyField(Project)

    def __str__(self):
        return self.name
