#views.py
from .models import Temple
from .serializers import TempleSerializer

from rest_framework import generics

class TempleList (generics.ListAPIView):
    queryset = Temple.objects.all()
    serializer_class = TempleSerializer
