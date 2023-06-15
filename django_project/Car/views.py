from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CarSerializer
from .models import Car

class CarList(APIView):
    def get(self, request):
        cars = []
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)

class CarCreate(APIView):
    def post(self, request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CarDelete(APIView):
    def delete(self, request, car_id):
        try:
            car = Car.objects.get(pk=car_id)
        except Car.DoesNotExist:
            return Response({'error': 'Car not found'}, status=status.HTTP_404_NOT_FOUND)
        
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'car_list.html', {'cars': cars})
