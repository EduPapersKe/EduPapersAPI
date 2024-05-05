from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import login, authenticate, logout

from .models import User
from .serializers import UserSerializer, LoginSerializer


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    @action(methods=['POST'], detail=False)
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        self.perform_create(serializer)
        
        user = serializer.instance
        user_id = user.id
        response_data = {'user_id': user_id}
        headers = self.get_success_headers(response_data)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    
    @action(methods=['GET'], detail=True)
    def retrieve(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
        
    @action(methods=['PUT'], detail=True)
    def update(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    
    @action(methods=['PATCH'], detail=True)  
    def partial_update(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
        
        
    @action(methods=['DELETE'], detail=True)
    def destroy(self, request, pk=None):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class LoginView(APIView):
    serializer_class = LoginSerializer
    
    @action(methods=['POST'], detail=False)
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_verified is True:
                    login(request, user)
                    refresh = RefreshToken.for_user(user)
                    token = str(refresh.access_token)
                    return Response({'token': token, 'user': user.id}, status=status.HTTP_200_OK)
                else:
                    return Response({'error': 'Your account needs to be verified to log in.'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)