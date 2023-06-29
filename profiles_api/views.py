from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP method as function (get, post, patch, put, delete)',
            'Is Simila to a traditional django view',
            'Gives you most control over the application logic',
            'Is mapped to URLs',
        ]

        return Response({'message' : 'Hello!', 'an_apiview': an_apiview})

