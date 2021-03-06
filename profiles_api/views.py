from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework import status,viewsets,filters
from rest_framework.permissions import IsAuthenticated

from profiles_api import serializers,models,permissions

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

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self,request):
        """Return hello message"""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLS using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self,request):
        """Create a new hello message"""
        Tserializer = self.serializer_class(data=request.data)

        if Tserializer.is_valid():
            name = Tserializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'msg':message})
        else:
            return Response(Tserializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request, pk=None):
        """Handle getting an object by its ID"""
        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        """Handle updating object"""
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        """Handle updating  part of an object"""
        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        """Handle removing an object"""
        return Response({'http_method':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handle creating,reading and updting profile feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.FeedItemProfileSerializer
    queryset = models.FeedItemProfile.objects.all()
    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticated
    )

    # override behaviour of creating new model in viewset
    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile = self.request.user)