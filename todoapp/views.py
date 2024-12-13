from django.shortcuts import render
from rest_framework import serializers
from todoapp.models import TodoListModel
from todoapp.serializers import ToDoListSerializer
from rest_framework import viewsets
# for custom views
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class TodolistApis(viewsets.ModelViewSet):
    queryset= TodoListModel.objects.all()
    serializer_class=ToDoListSerializer

@api_view(['GET'])
def completed_tasks(request):
    todos = TodoListModel.objects.filter(is_completed = True)
    serializer = ToDoListSerializer(todos, many=True)
    return Response(serializer.data, status.HTTP_200_OK)