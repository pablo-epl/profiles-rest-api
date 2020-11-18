from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            "Uses HTTP methods as function (get, post, patch, put, delete)",
            "Is similar to a traditional Django View",
            "Gives you the most control over your application logic",
            "Is mapped manually to URLs"
        ]
        return Response({"message": "Hello!", "an_apiview": an_apiview})

    def post(self, request):
        """Creates a Hello Message with our name, last name and email"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            last_name = serializer.validated_data.get('last_name')
            email = serializer.validated_data.get('email')

            message = f'Hello {name} {last_name}, {email}'
            return Response({"message": message})
        else:
            return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, primary_key=None):
        """Handles updating an object"""
        return Response({"method": "PUT"})

    def patch(self, request, primary_key=None):
        """Handles a partial update of an object"""
        return Response({"method": "PATCH"})

    def delete(self, request, primary_key=None):
        """Deletes an object"""
        return Response({"method": "DELETE"})
