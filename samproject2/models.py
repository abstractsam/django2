# Responsible for making tables in the database
# The class should be typed singular but will appear plural in database
from django.db import models


class People(models.Model):
    model = models.CharField(max_length=30, blank=False, null=False)
    location = models.CharField(max_length=30)
    year = models.IntegerField(default=1)
    cartype = models.CharField(max_length=30)
    price = models.IntegerField(default=1)


def __str__(self):
    return self.name
