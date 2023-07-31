# Responsible for making tables in the database
# The class should be typed singular but will appear plural in database
from django.db import models


class People(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField()
    phone = models.IntegerField(default=1)
    country = models.CharField(default='Kenya', max_length=30)
    city = models.CharField(default='Nairobi', max_length=30)
    age = models.IntegerField()
    gender = models.CharField(max_length=30, blank=False, null=False)


def __str__(self):
    return self.name
