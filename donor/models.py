from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User


class Donar(models.Model):
    choice = (('Male', 'Male'),
              ('Female', 'Female'),
              )
    choice1 = (('O Positive', 'O Positive'),
               ('O Negative', 'O Negative'),
               ('A Positive', 'A Positive'),
               ('A Negative', 'A Negative'),
               ('B Positive', 'B Positive'),
               ('B Negative', 'B Negative'),
               ('AB Negative', 'AB Negative'),
               ('AB Positive', 'AB Positive'),
               )
    Donar_name = models.CharField(max_length=50, blank=False, null=False, default=' ')
    gender = models.CharField(max_length=20, choices=choice, default='Male')
    age = models.IntegerField(validators=[MinValueValidator(18)])
    blood_group = models.CharField(max_length=20, choices=choice1, default='O Positive')
    email = models.EmailField()
    mobile = models.CharField(max_length=10, default=' ', null=True, blank=True)
    address = models.CharField(max_length=40)


class BloodDonate(models.Model):
    donor = models.ForeignKey(Donar, on_delete=models.CASCADE)
    disease = models.CharField(max_length=100, default="Nothing")
    age = models.PositiveIntegerField()
    bloodgroup = models.CharField(max_length=10)
    unit = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=20, default="Pending")
    date = models.DateField(auto_now=True)


