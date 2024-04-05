from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.
@api_view(['GET'])
def get_all_area_market_list(request):
    all_markets = MarketAreaCluster.objects.all()
    all_markets_serializer = MarketAreaClusterSerializer(all_markets,many=True)
    return Response(all_markets_serializer.data)