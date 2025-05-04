from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer
# Create your views here.


class TaskView(APIView):
    
    def get(self, request,pk=None):
        if pk:
            try:

                task= Task.objects.get(pk=pk)
            except:
                return Response({'message':'this task not found'},status=status.HTTP_404_NOT_FOUND)

           
            serializer = TaskSerializer (task)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:

            tasks = Task.objects.all()
            serializer = TaskSerializer(tasks,many = True)

            return Response(serializer.data,status=status.HTTP_200_OK)
            

    def post(self,request):
        data =request.data
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk):
        try:

            task= Task.objects.get(pk=pk)
        except:
            return Response({'message':'this task not found'},status=status.HTTP_404_NOT_FOUND)

        serializer = TaskSerializer(
            instance=task,
            data= request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.error_messages,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):

        try:
            task=Task.objects.get(pk=pk)
        except:
            return Response({
                "message":"no task found",
            },status=status.HTTP_404_NOT_FOUND)
        
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    



    
    