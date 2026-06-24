from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Expense
from django.shortcuts import get_list_or_404

# Create your views here.
@csrf_exempt
def expense_api(request):
    if request.method == 'GET':
        expenses = Expense.objects.all() #Fetches all Expenses table from models

        data = []
        for e in expenses:#converting rows into list dictionary
            data.append({
                "id": e.id,
                "title": e.title,
                "amount": float(e.amount),
                "category": e.category,
                "date_added": e.date_added.strftime('%Y-%m-%d %H:%M:%S')
            })

        return JsonResponse(data, safe=False)
        

    elif request.method == 'POST':

        #read and decode raw network bytes
        body_text = request.body.decode('utf-8')
        body_data = json.loads(body_text)

        #Insert data into SQLite table
        new_expense = Expense.objects.create(
            title = body_data['title'],
            amount = body_data['amount'],
            category = body_data['category']
        )

        return JsonResponse({
            "message": "Expense added successfully!",
            "id": new_expense.id
        }, status = 201)

@csrf_exempt
def expense_detail(request, id):
    # 1. Find the item or return a clean 404
    try:
        expense = Expense.objects.get(id=id)
    except Expense.DoesNotExist:
        return JsonResponse({"error": "Expense not found!"}, status=404)

    # 2. Handle GET
    if request.method == 'GET':
        return JsonResponse({
            "id": expense.id,
            "title": expense.title,
            "amount": float(expense.amount),
            "category": expense.category,
            "date_added": expense.date_added.strftime('%Y-%m-%d %H:%M:%S')
        })

    # 3. Handle DELETE
    elif request.method == 'DELETE':
        expense.delete()
        return JsonResponse({"message": "Expense deleted successfully!"}, status=200)

    # 4. SAFETY NET: If someone sends a PUT, PATCH, or anything else, 
    # return a clean HTTP 405 Method Not Allowed instead of throwing a ValueError crash!
    return JsonResponse({"error": f"Method {request.method} not allowed"}, status=405)