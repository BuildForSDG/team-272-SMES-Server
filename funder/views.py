from rest_framework import generics

from .models import Funder
from .serializers import FunderSerializer

# Create your views here.

class FunderList(generics.ListCreateAPIView):
    queryset = Funder.objects.all()
    serializer_class = FunderSerializer

class FunderDetail(generics.RetrieveAPIView):
    queryset = Funder.objects.all()
    serializer_class = FunderSerializer

class FunderUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Funder.objects.all()
    serializer_class = FunderSerializer