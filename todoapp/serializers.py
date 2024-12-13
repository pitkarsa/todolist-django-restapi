from rest_framework import serializers
from todoapp.models import TodoListModel

class ToDoListSerializer(serializers.ModelSerializer):
    class Meta:
        model=TodoListModel
        fields = ['id','title','description','is_completed']
# above code works for all HTTP 
#patch reuest: from postman
# http://localhost:8000/apis/todolist/1/ (here, remeber that last '/' is must )  and send the body {"is_completed":true}



#for custom urls and views 
# class ToDoListSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model=TodoListModel
#         fields = ['url','id','title','description','is_completed']