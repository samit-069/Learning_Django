from django.urls import path
from .views import expense_api, expense_detail

app_name = "core"

urlpatterns = [
    # Think of this file as standing INSIDE the "/api/expenses/" room already.
    path('', expense_api),                  # Maps to: /api/expenses/
    path('<int:id>/', expense_detail),       # Maps to: /api/expenses/<int:id>/
]