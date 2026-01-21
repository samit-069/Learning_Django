import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Student


@csrf_exempt
def students_list(request):
    if request.method == "GET":
        students = Student.objects.all().values()
        return JsonResponse(list(students), safe=False)

    if request.method == "POST":
        try:
            data = json.loads(request.body)

            student = Student.objects.create(
                roll=data["roll"],
                name=data["name"],
                marks=data["marks"]
            )

            return JsonResponse(
                {
                    "id": student.id,
                    "roll": student.roll,
                    "name": student.name,
                    "marks": student.marks
                },
                status=201
            )

        except KeyError:
            return JsonResponse({"error": "Missing fields"}, status=400)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

    return JsonResponse({"error": "Method not allowed"}, status=405)
