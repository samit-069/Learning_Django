from django.urls import path
from .views import expense_api, expense_detail, expense_total_api, expense_list_view

app_name = "core"

urlpatterns = [
    # Think of this file as standing INSIDE the "/api/expenses/" room already.
    path('', expense_api),
    path('<int:id>/', expense_detail),
    path('total/', expense_total_api),
    path('web/',expense_list_view)
]