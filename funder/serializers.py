from rest_framework import serializers

from .models import Funder


class FunderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funder
        fields = '__all__'