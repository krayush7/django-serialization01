from rest_framework import serializers
from .models import *

class StudentSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=50)