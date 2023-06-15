from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AnimalSerializer
from .models import Animal 

class AnimalList(APIView): 
    def get(self, request):
        animals = []
        serializer = AnimalSerializer(animals, many=True)
        return Response(serializer.data)

class AnimalCreate(APIView):
    def post(self, request):
        serializer = AnimalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

class AnimalDelete(APIView):
    def delete(self, request, animal_id):
        try:
            animal = Animal.objects.get(pk=animal_id)
        except Animal.DoesNotExist:
            return Response({'error': 'Animal not found'}, status=status.HTTP_404_NOT_FOUND)
        
        animal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def animal_list(request):
    animals = Animal.objects.all()
    return render(request, 'animal_list.html', {'animals': animals})        
