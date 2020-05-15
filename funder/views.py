from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth import  authenticate

from .models import Funder
from .serializers import FunderCreateUserSerializer, FunderSerializer

# Create your views here.

class FunderLogin(APIView):
    permission_classes = ()

    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)

class FunderSignup(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = FunderCreateUserSerializer

class FunderList(generics.ListCreateAPIView):
    queryset = Funder.objects.all()
    serializer_class = FunderSerializer


class FunderProfile(generics.RetrieveAPIView):
    queryset = Funder.objects.all()
    serializer_class = FunderSerializer

class FunderProfileUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Funder.objects.all()
    serializer_class = FunderSerializer