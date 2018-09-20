from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloApiView(APIView):
    """Test API View"""
    def get(self, request, format=None):
        """Returns a list of APIView features."""
        an_apiview = [
            'Uses HTTP methods as function(get, post, patch, put, delete)',
            'Similar to traditional django view',
            'Gives the most control over the logic',
            'Is mapped mannually to the URLs'
        ]
        return Response({'Message ': "My First APIView!!", 'an_apiview': an_apiview})
