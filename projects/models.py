from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Technologie(models.Model):

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)


class Project(models.Model):
    STATUS = (
        ('S','in-progress'),
        ('P','paused'),
        ('F','finished'),
        ('D','delivered')
    )

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=600)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=1, choices=STATUS, default='S')
    tecnologies = models.ManyToManyField(Technologie)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

