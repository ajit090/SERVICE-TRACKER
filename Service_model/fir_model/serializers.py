from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Fir,Techtracker 


class FirSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fir
        fields = '__all__' 

class TechtrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Techtracker
        fields = '__all__' 