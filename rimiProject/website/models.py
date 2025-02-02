from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=50)
    college=models.CharField(max_length=100)
    age=models.IntegerField(max_length=3)
    is_active=models.BooleanField(default=False)