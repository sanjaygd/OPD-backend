from rest_framework.serializers import ModelSerializer

from .models import PatientVisit, Doctor
from patient_info.models import Patient, Address
from patient_info.serializers import PatientCreateSerializer, AddressCreateSerializer


class VisitSerializer(ModelSerializer):
    patient = PatientCreateSerializer(many=False)

    class Meta:
        model = PatientVisit
        fields = ['patient','reason', 'visited',]
        order = -1

    def create(self, validated_data):
        patient_obj_data = validated_data.pop('patient')

        patient_instance = Patient.objects.create(
            name = patient_obj_data['name'],
            mobile_number = patient_obj_data['mobile_number'],
            DOB = patient_obj_data['DOB'],
            blood_group = patient_obj_data['blood_group'],
            
            
        )
        address = patient_obj_data['address']
        
        address_instance = Address.objects.create(home_number = address['home_number'],
                               street_name = address['street_name'], 
                               area_or_village = address['area_or_village'], 
                               taluk = address['taluk'], 
                               district=address['district'], 
                               pin = address['pin'])
        patient_instance.address = address_instance
        patient_instance.save()
        
        patient_visit_instance = PatientVisit.objects.create( 
                        **validated_data,
                        patient = patient_instance)
        patient_visit_instance.save()
        if  validated_data.get('doctor'):
            patient_visit_instance.doctor.add(validated_data.get('doctor')[0])
        
        return patient_visit_instance

        

class DoctorSerializer(ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'


class DoctorListSerializer(ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
        


