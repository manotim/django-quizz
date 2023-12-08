from django.db import models
from django.utils import timezone

# Create your models here.
class Risk(models.Model):
    position = models.IntegerField()
    icon = models.CharField(max_length=100)
    risk_description = models.CharField(max_length=255)
    date_posted = models.DateTimeField(default=timezone.now)

class Service(models.Model):
    description = models.TextField()

class Package(models.Model):
    package_name = models.CharField(max_length=255)
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    days = models.IntegerField()
    services = models.ManyToManyField(Service)

