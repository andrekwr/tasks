from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from tasks.models import Task
from django.core.serializers import serialize
from rest_framework.parsers import JSONParser
from tasks.serializer import TaskSerializer
from rest_framework.response import Response



# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")

@api_view(["GET"])
def get_tasks(request):
    tasks = serializers.serialize("json", Task.objects.all())
    return HttpResponse(tasks, content_type="application/json")


@api_view(["GET"])
def get_task(request, id_):
    try:
        return JsonResponse(model_to_dict(Task.objects.get(pk=id_)), safe=False)
    except Task.DoesNotExist:
        raise HttpResponse(status=404)


@api_view(["POST"])
def create_task(request):
	serializer = TaskSerializer(data=request.data)
	if serializer.is_valid():
	    serializer.save()
	    return Response(serializer.data, status=status.HTTP_201_CREATED)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
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
def delete_task(request, pk):
	try:
        task = Task.objects.get(pk=pk)
        task.delete()
        return HttpResponse("Task deleted", content_type="application/json")
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["DELETE"])
def delete_all(request, pk):
	try:
        task = Task.objects.get(pk=pk)
        task.delete()
        return HttpResponse("Task deleted", content_type="application/json")
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)