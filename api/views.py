from pytz import UTC
from rest_framework import status
from .serializer import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
import datetime
# Create your views here.

@api_view(['GET'])
def AllTask(request):
    a = Task.objects.all()
    ser = TaskSer(a, many=True)

    return Response(ser.data)


@api_view(['GET'])
def Search_Task(request):
    search = request.GET['search']
    a = Task.objects.filter(name__icontains=search)
    ser = TaskSer(a, many=True)

    return Response(ser.data)

@api_view(['POST'])
def Create_Task(request):
    name = request.POST.get('name')
    a = Task.objects.create(name=name)
    ser = TaskSer(a)

    return Response(ser.data)

@api_view(['GET'])
def Delete_Task(request):
    task_id = request.GET['id']
    task = Task.objects.get(id=task_id)
    task.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def Edit_Task(request):
    task_id = request.GET['id']
    task = Task.objects.get(id=task_id)
    task.status = True
    task.save()

    return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def Filter_Status_Task(request):
    status = request.GET['status']
    task = Task.objects.filter(status=status)
    ser = TaskSer(task, many=True)

    return Response(ser.data)

@api_view(['GET'])
def Filter_Date_Task(request):
    start = request.GET['start']
    end = request.GET['end']
    task = Task.objects.filter(date__gte=start, date__lte=end)
    ser = TaskSer(task, many=True)

    return Response(ser.data)