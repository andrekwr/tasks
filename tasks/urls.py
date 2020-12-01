from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("list", views.get_tasks, name="GetAllTasks"),
    path("list/<int:pk>", views.get_task, name="GetATask"),
    path("create", views.create_task, name="CreateTask"),
    path("update/<int:pk>", views.update_task, name="UpdateTask"),
    path("delete/<int:pk>", views.delete_task, name="DeleteATask"),
    path("delete", views.delete_all, name="DeleteTasks"),
]
