from django.urls import path
from .views import expense_api, expense_detail, expense_total_api, expense_list_view,expense_list_drf,expense_detail_drf

app_name = "core"

urlpatterns = [
    # Think of this file as standing INSIDE the "/api/expenses/" room already.
    path('', expense_api, name='expense_api'),
    path('<int:id>/', expense_detail, name='expense_detail'),
    path('total/', expense_total_api, name='expense_total_api'),
    path('web/',expense_list_view, name='expense_list_view'),
    path('drf/',expense_list_drf, name='expense_list_drf'),
    path('drf/<int:pk>/',expense_detail_drf, name='expense_detail_drf'),
]