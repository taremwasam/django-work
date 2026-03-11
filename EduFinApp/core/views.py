from django.shortcuts import get_object_or_404 
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from core.models import Testing
from core.serializers import TestingSerializer

def testing_view(request):
    return JsonResponse({'message': 'Hello, world!'})

def health_check(request):
    return JsonResponse({'status': 'ok'})


def testing_detail_view(request, id):
    try:
        # Try to get the record
        testing_record = Testing.objects.get(id=id)
        serializer = TestingSerializer(testing_record)
        return JsonResponse(serializer.data)
    except Testing.DoesNotExist:
        # Return a custom JSON error response
        return JsonResponse(
            {'error': 'Record not found'}, 
            status=404
        )