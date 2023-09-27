from django.db import models

class contactFields(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)
    Phone=models.CharField(max_length=20)
    Website_Link=models.CharField(max_length=100)
    Country=models.CharField(max_length=50)
    Message=models.TextField()

# Create your models here.
