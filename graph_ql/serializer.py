from rest_framework import serializers
from . import models


class CheckNewModelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CheckNewModels
        fields = '__all__'

