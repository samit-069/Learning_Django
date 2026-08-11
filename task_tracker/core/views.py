from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializer import Taskseralizer

# Create your views here.
@api_view(['GET','POST'])
def task_list(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = Taskseralizer(tasks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = Taskseralizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def task_detail(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response({'error':'Task not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Taskseralizer(task)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Taskseralizer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)