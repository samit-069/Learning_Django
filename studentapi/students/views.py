from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Students
import json

# Create your views here.

@csrf_exempt
def student_list(request):
    if request.method == 'GET':
        students = Students.objects.all()
        student_data = [
            {
                'id': student.id,
                'name': student.name,
                'email': student.email,
                'enrolment_date': student.enrolment_date,
                'grade_level': student.grade_level,
                'is_active': student.is_active,
            }
            for student in students
        ]
        return JsonResponse({'students':student_data})

    elif request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        email = data.get('email')
        enrolment_date = data.get('enrolment_date')
        grade_level = data.get('grade_level')

        if not name:
            return JsonResponse({'error': 'Name is required'}, status=400)
        
        student = Students.objects.create(name=name, email=email, enrolment_date=enrolment_date, grade_level=grade_level,is_active=True)

        return JsonResponse({
            'id': student.id,
            'name': student.name,
            'email': student.email,
            'enrolment_date': enrolment_date,
            'grade_level': grade_level,            
        },status=201)
    
@csrf_exempt
def student_update(request,id):
    if request.method == 'PATCH':
        try:
            student = Students.objects.get(id=id)
        except Students.DoesNotExist:
            return JsonResponse({'error': 'Student not found'}, status=404)
        
        data = json.load(request.body)
        #do updates WIP

        student.save()

        return JsonResponse({'message':'Data Updated'})
    
    elif request.method == 'DELETE':
        try:
            student = Students.objects.get(id=id)
        except Students.DoesNotExist:
            return JsonResponse({'error': 'Student not found'}, status=404)

        student.delete()
        return JsonResponse({'message': 'Student deleted'})