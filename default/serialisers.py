from rest_framework import serializers
from . models import *


class ServoSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Servo 
        fields = "__all__"