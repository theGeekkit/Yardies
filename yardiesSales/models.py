from django.db import models

# Create your models here.
class SaleSchedule(models.Model):    
    time = models.TimeField(blank = False)
    date = models.DateField(blank = False)
    
class SaleLocation(models.Model):
    state = models.CharField(max_length=50, blank = False)
    city = models.CharField(max_length=50, blank = False)
    street = models.CharField(max_length=50, blank = False, null = False)