from django.shortcuts import render
from .serializers import empSerializer
from .models import emp
from rest_framework import viewsets


class empViewSet(viewsets.ModelViewSet):
    
    queryset = emp.objects.all()
    
    serializer_class = empSerializer