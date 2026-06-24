from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Task
import json

@csrf_exempt
def task_update(request, id):
    if request.method == 'PATCH':
        try:
            task = Task.objects.get(id=id)
        except Task.DoesNotExist:
            return JsonResponse({'error': 'Task not found'}, status=404)
        
        data = json.loads(request.body)
        completed = data.get('completed')
        
        task.completed = completed
        task.save()
        
        return JsonResponse({  # ← MUST return something
            'id': task.id,
            'title': task.title,
            'completed': task.completed,
        })
    elif request.method == 'DELETE':
        try:
            task = Task.objects.get(id=id)
        except Task.DoesNotExist:
            return JsonResponse({'error': 'Task not found'}, status=404)

        task.delete()
        return JsonResponse({'message': 'Task deleted'})

@csrf_exempt
def task_list(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        task_data = [
            {
                'id': task.id,
                'title': task.title,
                'completed': task.completed,
            }
            for task in tasks
        ]
        return JsonResponse({'tasks': task_data})

    elif request.method == 'POST':
        data = json.loads(request.body)
        title = data.get('title')
        
        if not title:
            return JsonResponse({'error': 'Title is required'}, status=400)
        
        task = Task.objects.create(title=title, completed=False)
        
        return JsonResponse({
            'id': task.id,
            'title': task.title,
            'completed': task.completed,
        }, status=201)
