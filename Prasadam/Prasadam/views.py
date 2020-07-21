#views.py
from .models import Temple
from .serializers import TempleSerializer

from rest_framework import generics

class TempleList (generics.ListCreateAPIView):
    queryset = Temple.objects.all()
    serializer_class = TempleSerializer

class TempleDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Returns a single Temple and allows updates and deletion of a Task.
    """
    queryset = Temple.objects.all()
    serializer_class = TempleSerializer
    lookup_url_kwarg = 'temple_id'
