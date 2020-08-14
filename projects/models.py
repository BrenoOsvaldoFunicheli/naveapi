from django.contrib.auth.models import User
from django.db import models


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
    active = models.CharField(max_length=1, choices=REGISTER_STATUS, default='A')
    creator = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
