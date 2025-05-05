from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class TaskView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request,pk=None):
        if pk:
            try:

                task= Task.objects.get(pk=pk)
            except:
                return Response({'message':'this task not found'},status=status.HTTP_404_NOT_FOUND)

            if request.user != task.owner:
                return Response (
                    {
                        "message":"You ar not the owner of this task"
                    },
                    status=status.HTTP_401_UNAUTHORIZED
                )

            serializer = TaskSerializer (task)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:

            if  not request.user.is_staff :
                return Response(
                    {
                        "message":"Only Admins Can view All Tasks"
                    },
                    status=status.HTTP_403_FORBIDDEN
                )

            tasks = Task.objects.all()
            serializer = TaskSerializer(tasks,many = True)

            return Response(serializer.data,status=status.HTTP_200_OK)
            

    def post(self,request):
        data =request.data
        data['owner']=request.user.id
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk):
        try:

            task= Task.objects.get(pk=pk)
        except:
            return Response({'message':'this task not found'},status=status.HTTP_404_NOT_FOUND)
        
        if request.user != task.owner:
            return Response(
                {
                    "message":"You Cant Edit This Task"
                },
                status=status.HTTP_401_UNAUTHORIZED
            )

        serializer = TaskSerializer(
            instance=task,
            data= request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):

        try:
            task=Task.objects.get(pk=pk)
        except:
            return Response({
                "message":"no task found",
            },status=status.HTTP_404_NOT_FOUND)
        
        if request.user != task.owner:
            return Response(
                {
                    "message":"You Cant delete This Task"
                },
                status=status.HTTP_403_FORBIDDEN
            )
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def task_complet(request,pk):
    try:
        task=Task.objects.get(pk=pk)
    except:
        return Response(
            {
                "message":"This task isn't exist"
            },
            status=status.HTTP_404_NOT_FOUND
        )
    if request.user != task.owner:
            return Response(
                {
                    "message":"You Cant Mark This Task As completed"
                },
                status=status.HTTP_403_FORBIDDEN
            )
    task.completed = not task.completed
    task.save()
    return Response(TaskSerializer(task).data, status=status.HTTP_200_OK)


    
    