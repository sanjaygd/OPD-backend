from rest_framework import serializers

from .models import Patient, Address


class AddressCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class PatientCreateSerializer(serializers.ModelSerializer):
    address = AddressCreateSerializer(many=False)
    class Meta:
        model = Patient
        fields = ['name', 'mobile_number', 'DOB', 'blood_group', 'address']
    
    def create(self, validated_data):
        patient_address_obj = validated_data.pop('address')
        address_instance = Address.objects.create(
           home_number = patient_address_obj['home_number'],
           street_name = patient_address_obj['street_name'],
           area_or_village = patient_address_obj['area_or_village'],
           taluk = patient_address_obj['taluk'],
           district = patient_address_obj['district'],
           pin = patient_address_obj['pin'],
        )
        address_instance.save()

        patient_instance = Patient.objects.create(
            **validated_data,
            address = address_instance
        )
        patient_instance.save()
        return patient_instance
    





