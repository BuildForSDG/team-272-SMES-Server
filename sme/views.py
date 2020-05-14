from rest_framework import generics

from .models import SME
from .serializers import SMESerializer

# Create your views here.

class SMEList(generics.ListCreateAPIView):
    queryset = SME.objects.all()
    serializer_class = SMESerializer

class SMEDetail(generics.RetrieveAPIView):
    queryset = SME.objects.all()
    serializer_class = SMESerializer

class SMEUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = SME.objects.all()
    serializer_class = SMESerializer