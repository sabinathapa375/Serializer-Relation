from django.shortcuts import render
from .models import Singer , Song
from .serializers import SongSerializer, SingerSerializer
from rest_framework.viewsets import ModelViewSet
# Create your views here.

class SingerViewSet(ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer
    
class SongViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    
    