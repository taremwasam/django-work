from django.http import JsonResponse
from django.shortcuts import render
from core.models import Testing
from django.http import HttpResponse

def health_check(request):
    return HttpResponse("Server is running!")

def testing_view(request):
    # For now, return a simple static JSON response
    return JsonResponse({'message': 'Hello, world!'})