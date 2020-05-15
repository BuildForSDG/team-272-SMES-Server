from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import Funder



class FunderCreateUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Funder
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        user = Funder(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user
        


class FunderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funder
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}