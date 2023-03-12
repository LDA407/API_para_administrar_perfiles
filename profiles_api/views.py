from rest_framework.views import APIView
from rest_framework.response import Response
from profiles_api import serializers, models, permissions
from rest_framework import status, viewsets, filters, authentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class HelloApiView(APIView):
    serializer_class=serializers.HelloSerializer

    def get(self, request, format=None):
        an_apiview = [
            'metodos http como funcionies ( post, get, put, delete)',
            'Nos da mayor control sobre la logica de la vista en la app',
            'Esta mapeado manualmente a los URLs'
        ]
        return Response({'message': 'hellow', 'an_apiview': an_apiview})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        return Response({'method': 'PUT'})

    def patch(sefl, request, pk=None):
        """actualizacion parcial de un objeto"""
        return Response({'method': 'PATCH'})

    def delete(sefl, request, pk=None):
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    serializer_class=serializers.HelloSerializer
    def list(self, request):
        a_viewset=[
            'usa las acciones estandar (post, create, retrieve, update, parcial_update, destroy)',
            'mapea las url automaticamente usando routers','Provee mas funcionalidad con menos codigo',]
        return Response({'message': 'hola!', 'a_viewset': a_viewset})

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST )

    def retrieve(self, request, pk=None):
        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        return Response({'http_method':'PATH'})

    def destroy(self, request, pk=None):
        return Response({'http_method': 'DELETE'})

 
class UserProfilViewSet(viewsets.ModelViewSet):
    serializer_class=serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    authentication_class = (authentication.TokenAuthentication,)
    permissions_class = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    renderer_class = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    authentication_class = (authentication.TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permissions_class = (permissions.UpdateOwnStatus, IsAuthenticated)

    def perform_create(self, serializers):
        """setea el perfil del usuario que se ha logeado"""
        serializers.save(user_profile=self.request.user)