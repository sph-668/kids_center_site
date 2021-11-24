from django.db import models
from django.conf import settings
from django.utils import timezone

class Mytimetable(models.Model):
    date = models.DateField()
    time = models.TimeField()
    teacher = models.TextField()
    group = models.TextField()
    lesson = models.TextField()
    cabinet = models.IntegerField()
    age = models.NOT_PROVIDED()

    def show(self):
        pass



# Create your models here.
