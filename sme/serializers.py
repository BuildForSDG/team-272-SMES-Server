from rest_framework import serializers

from .models import SME


class SMESerializer(serializers.ModelSerializer):
    class Meta:
        model = SME
        fields = '__all__'