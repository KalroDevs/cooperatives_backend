from django.shortcuts import render

from rest_framework import viewsets
from .models import Cooperative
from .serializers import CooperativeSerializer

class CooperativeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A viewset for viewing and editing cooperative instances.
    """
    serializer_class = CooperativeSerializer
    queryset = Cooperative.objects.all()