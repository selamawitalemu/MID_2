from rest_framework import serializers
from .models import emplo


class emploSerializer(serializers.ModelSerializer):
    class Meta:
        model = emplo
        fields ='__all__'