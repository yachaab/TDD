

# app/drf_project/views.py

from django.http import JsonResponse
from django.urls import reverse

def ping(request):
    data = {"ping": "pong!"}
    print('URL:', reverse("ping"))
    return JsonResponse(data)
