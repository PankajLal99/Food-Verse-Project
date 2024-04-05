from rest_framework import serializers
from .models import *

class MarketAreaClusterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketAreaCluster
        fields = ('title','location')