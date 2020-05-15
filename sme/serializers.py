from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import SME

class SMECreateUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SME
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = SME(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user
        
class SMESerializer(serializers.ModelSerializer):
    class Meta:
        model = SME
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}