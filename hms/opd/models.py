from django.db import models

from patient_info.models import Patient

class Doctor(models.Model):
    name = models.CharField(max_length=30)
    speciality = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=12)

    def __str__(self) -> str:
        super().__str__()
        return self.name

class PatientVisit(models.Model):
    patient         = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    reason          = models.CharField(max_length=50)
    doctor          = models.ManyToManyField(Doctor)
    visited         = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        super().__str__()
        return f"{self.patient} visited on {self.visited}"


class Address(models.Model):
    home_number = models.IntegerField()
    street = models.CharField(max_length=100)
    taluk = models.TextField(max_length=50)
    district = models.TextField(max_length=50)
    state = models.TextField(max_length=20)
    pin = models.IntegerField()






