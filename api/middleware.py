from django.http import JsonResponse
from rest_framework import status

from users.models import APIKey

class ClientMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        api_key = request.headers.get('API-KEY')

        if api_key:
            try:
                api_key_obj = APIKey.objects.get(api_key=api_key)
            except APIKey.DoesNotExist:
                return JsonResponse({'error': 'Invalid API key.'}, status=status.HTTP_403_FORBIDDEN)
        else:
            return JsonResponse({'error': 'Authentication keys not provided.'}, status=status.HTTP_403_FORBIDDEN)
        
        response = self.get_response(request)
        return response
