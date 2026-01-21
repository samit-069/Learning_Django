from django.urls import path
from .views import students_list

urlpatterns = [
    path('students/', students_list)
]