from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list),  # /api/tasks/ → task_list()
      path('<int:id>/', views.task_update)
]