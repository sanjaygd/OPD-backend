from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
                        CreateAPIView, 
                        ListAPIView, 
                        ListCreateAPIView,
                        )

from .models import PatientVisit, Doctor
from .serializers import VisitSerializer, DoctorSerializer, DoctorListSerializer


from rest_framework.authentication import SessionAuthentication, BasicAuthentication 

class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return

class VisitListView(ListAPIView):
    queryset = PatientVisit.objects.all()
    serializer_class = VisitSerializer



class CreateVisitApiView(ListCreateAPIView):
    queryset = PatientVisit.objects.all()
    serializer_class = VisitSerializer
    # authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

@method_decorator(csrf_exempt, name='dispatch')
class CreateDoctorApiView(CreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # super().create(request, **kwargs)
        return self.create(request, *args, **kwargs)


class ListDoctorApiView(ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorListSerializer
    permission_classes = [IsAuthenticated]


