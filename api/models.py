from django.db import models
import datetime
# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField(default=datetime.date.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name