from rest_framework import serializers
from .models import RGB

class RGBSerializer(serializers.ModelSerializer):
    class Meta:
        model = RGB
        fields ="__all__"
