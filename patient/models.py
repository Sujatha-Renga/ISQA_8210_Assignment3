from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    bloodgroup = models.CharField(max_length=10)
    disease = models.CharField(max_length=100)
    doctorname = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=False)
