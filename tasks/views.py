from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from tasks.models import Task
from django.core import serializers
from rest_framework.parsers import JSONParser
from tasks.serializer import TaskSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from django.forms.models import model_to_dict
from rest_framework.permissions import IsAuthenticated



# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_tasks(request):
    tasks = serializers.serialize("json", Task.objects.all())
    return HttpResponse(tasks, content_type="application/json")


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_task(request, pk):
    try:
        return JsonResponse(model_to_dict(Task.objects.get(pk=pk)), safe=False)
    except Task.DoesNotExist:
        raise HttpResponse(status=404)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_task(request):
	serializer = TaskSerializer(data=request.data)
	if serializer.is_valid():
	    serializer.save()
	    return Response(serializer.data, status=status.HTTP_201_CREATED)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_task(request, pk):

	try:
		task = Task.objects.get(pk=pk)
	except Task.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	serializer = TaskSerializer(task, data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_task(request, pk):
	try:
		task = Task.objects.get(pk=pk)
		task.delete()
		return HttpResponse("Task deleted", content_type="application/json")
	except Task.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_all(request):
	try:
		tasks = Task.objects.all()
		tasks.delete()
		return HttpResponse("Tasks deleted", content_type="application/json")
	except Task.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)