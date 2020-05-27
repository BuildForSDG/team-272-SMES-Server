from rest_framework import generics
# from rest_framework.generics import GenericAPIView
# from rest_framework.views import APIView
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.exceptions import PermissionDenied
# from django.contrib.auth import  authenticate


from .models import SME
from .serializers import SMECreateUserSerializer, SMESerializer

# Create your views here.


# class SMELogin(APIView):
#     permission_classes = ()

#     def post(self, request,):
#         username = request.data.get("username")
#         password = request.data.get("password")
#         user = authenticate(username=username, password=password)
#         if user:
#             return Response({"token": user.auth_token.key})
#         else:
#             return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)

class SMESignup(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = SMECreateUserSerializer

class SMEList(generics.ListCreateAPIView):
    queryset = SME.objects.all().order_by('date_joined')
    serializer_class = SMESerializer

class SMEProfile(generics.RetrieveAPIView):
    queryset = SME.objects.all()
    serializer_class = SMESerializer

class SMEProfileUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = SME.objects.all()
    serializer_class = SMESerializer
