from rest_framework import serializers

from .models import emp

class empSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = emp
        fields = ('title', 'description')