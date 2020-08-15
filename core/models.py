from django.db import models

#   needed imports
from django.contrib.auth.models import User


# Create your models here.


class JobRole(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name


# Create your models here.
class Technologie(models.Model):

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Project(models.Model):
    STATUS = (
        ('C', 'in-progress'),
        ('P', 'paused'),
        ('F', 'finished'),
    )

    REGISTER_STATUS = (
        ('A', 'Actived'),
        ('D', 'Deleted')
    )

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=600)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS, default='C')
    tecnologies = models.ManyToManyField(Technologie)
    active = models.CharField(
        max_length=1, choices=REGISTER_STATUS, default='A')
    creator = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class NaverDateQuerySet(models.QuerySet):
    def more_than(self, days):
        return self.raw('SELECT * FROM core_naver WHERE COALESCE(end_date,CURRENT_DATE)-admission_date > '+days)

    def equal(self, days):
        return self.raw('SELECT * FROM core_naver WHERE COALESCE(end_date,CURRENT_DATE)-admission_date = '+days)

    def less_than(self, days):
        return self.raw('SELECT * FROM core_naver WHERE COALESCE(end_date,CURRENT_DATE)-admission_date < '+days)

class NaverDateManager(models.Manager):
    def get_queryset(self):
        return NaverDateQuerySet(self.model, using=self._db)

    def more_than(self, days):
        return self.get_queryset().more_than(days)

    def equal(self, days):
        return self.get_queryset().equal(days)

    def less_than(self, days):
        return self.get_queryset().less_than()

class Naver(models.Model):

    #   need choices used to preserve deleted rows
    STATUS = (
        ('A', 'Actived'),
        ('D', 'Deleted')
    )

    #   model fields that represent table
    name = models.CharField(max_length=100)
    job_role = models.ForeignKey(JobRole, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=1, choices=STATUS, default='A')
    admission_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    projects = models.ManyToManyField(Project)
    creator = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)

    #   managers Definition
    objects = models.Manager()
    company_time = NaverDateManager()

    def __str__(self):
        return self.name

    #   Property that provide the name format insted of id
    @property
    def job(self):
        # return str(self.pk)
        return str(self.job_role)  # JobRole.objects.get(pk=self.job_role).name
