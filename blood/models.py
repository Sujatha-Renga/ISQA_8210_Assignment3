from django.db import models
from django.core.validators import MinValueValidator
from patient import models as pmodels
from donor import models as dmodels


# Create your models here.

class BloodStock(models.Model):
    blood_group = models.CharField(max_length=20)
    units = models.FloatField(default=0, validators=[MinValueValidator(0)])


class BloodRequest(models.Model):
    request_by_patient = models.ForeignKey(pmodels.Patient, null=True, on_delete=models.CASCADE)
    request_by_donor = models.ForeignKey(dmodels.Donar, null=True, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=30)
    patient_age = models.PositiveIntegerField()
    reason = models.CharField(max_length=500)
    bloodgroup = models.CharField(max_length=10)
    unit = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=20, default="Pending")
    date = models.DateField(auto_now=True)


