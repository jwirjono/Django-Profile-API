from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        """Returns a list of APIView features"""
        an_apiview=[
            'Uses HTTP methods as function(get,post,patch,put,delete)',
            'is similar to a traditional django view',
            'gsagas',
            'gastwtq'
        ]

        return Response({'msg':'Hello!','api':an_apiview})

    def post(self,request):
        """Create a hello message with our name"""
        XXserializerXX = self.serializer_class(data=request.data)

        if XXserializerXX.is_valid():
            name = XXserializerXX.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'msg':message})
        else:
            return Response(XXserializerXX.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request, pk=None):
        """Handle updating object"""
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        """Handle partial object"""
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        """Delete object"""
        return Response({'method':'DELETE'})

            # status=400 juga bisa
