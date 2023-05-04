from django.shortcuts import render

from rest_framework import generics

from .models import Patient
from .serializers import PatientCreateSerializer


class CreatePatientApiView(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientCreateSerializer


