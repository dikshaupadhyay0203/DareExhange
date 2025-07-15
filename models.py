from django.db import models

# Create your models here.

class DareExchange(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    dare=models.TextField()
    deadline=models.DateField(blank=True,null=True)
    phone_number=models.CharField(max_length=10)
   

