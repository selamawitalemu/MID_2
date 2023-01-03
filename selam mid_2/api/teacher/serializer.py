from rest_framework import serializers
from .models import teac


class teacSerializer(serializers.ModelSerializer):
    class Meta:
        model = teac
        fields ='__all__'