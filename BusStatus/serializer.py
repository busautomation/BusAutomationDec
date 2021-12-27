from rest_framework import serializers
from .models import BusSatusData, SensorData

class BusSatusDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusSatusData
        fields = '__all__'
class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = '__all__'

