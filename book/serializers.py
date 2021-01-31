from rest_framework import serializers
from .models import contactBook

class contactBookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = contactBook
        fields = '__all__'