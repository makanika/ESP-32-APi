from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . models import *
from . serialisers import *

# Create your views here.
@api_view(["GET"])
def homeView(request):
    res = {
        "msg": "esp endpoints"
    }

    return Response(res, status=status.HTTP_200_OK)

@api_view(["GET", "POST"])
def servo(request):
    if request.method == "GET":
        rotations = Servo.objects.all()
        serialiser = ServoSerialiser(rotations, many=True)
        return Response(serialiser.data, status=status.HTTP_200_OK)
    else:
        data = request.data
        serialiser = ServoSerialiser(data=data)
        if serialiser.is_valid():
            serialiser.save()
            return Response(serialiser.data, status=status.HTTP_201_CREATED)
        return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)