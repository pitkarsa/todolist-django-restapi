from django.urls import path, include
from rest_framework.routers import DefaultRouter
from todoapp.views import TodolistApis,completed_tasks

router = DefaultRouter()
router.register(r'todolist',TodolistApis)

urlpatterns = [
   path('',include(router.urls)),
   path('completed',completed_tasks ),
]
