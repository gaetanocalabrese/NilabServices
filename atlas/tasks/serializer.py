from rest_framework import serializers
from .models import LongTask


class LongTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = LongTask
        fields = '__all__'