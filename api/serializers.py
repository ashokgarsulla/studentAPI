from rest_framework import serializers
from django import forms

from api.models import Stdnt
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 100)
    roll = serializers.IntegerField() 
# for creation
    def create(self, validate_data):
        return Stdnt.objects.create(**validate_data)

# for updation..
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll',instance.roll)
        instance.save()
        return instance

class StudentForms(forms.Form):
    name = forms.CharField(max_length = 100)
    roll = forms.IntegerField() 