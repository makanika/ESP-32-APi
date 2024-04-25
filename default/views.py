# from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . models import Servo
from . serialisers import ServoSerializer

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
        serializer = ServoSerializer(rotations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        data = request.data
        serializer = ServoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
