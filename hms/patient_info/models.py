from django.db import models

class Patient(models.Model):
    name            = models.TextField(max_length=30)
    mobile_number   = models.BigIntegerField()
    DOB             = models.DateField()
    blood_group     = models.TextField(max_length=4)
    address         = models.OneToOneField('Address', on_delete=models.CASCADE, null=True)

class Address(models.Model):
    home_number     = models.TextField(null=True, blank=True, max_length=10)
    street_name     = models.TextField(null=True, blank=True, max_length=20)
    area_or_village = models.TextField(max_length=20)
    taluk           = models.TextField(max_length=20)
    district        = models.TextField(max_length=20)
    pin             = models.IntegerField()





