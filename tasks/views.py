from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from tasks.models import Task
from django.core.serializers import serialize
from rest_framework.parsers import JSONParser



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



