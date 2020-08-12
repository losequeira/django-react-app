from rest_framework import serializers
from .models import Address, Student

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    address = AddressSerializer(many=False)
    class Meta:
        model = Student
        fields = ['id', 'name', 'lastname', 'birthdate', 'address']
    
    def create(self, validated_data):
        address_data = validated_data.pop("address")
        saved_address = Address.objects.create(**address_data)

        return Student.objects.create(
            address=saved_address,
            **validated_data
        )