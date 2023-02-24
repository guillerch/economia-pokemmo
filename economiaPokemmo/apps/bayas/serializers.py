from rest_framework import serializers
from .models import Baya

class BayaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Baya
        fields = '__all__'