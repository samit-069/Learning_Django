from django import path
from . import views

urlpatterns = [
    path('', views.student_list),
    path('<int:id>/',views.student_update)
]