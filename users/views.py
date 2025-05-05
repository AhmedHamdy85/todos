from django.shortcuts import render
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.

class UserRegesterView(APIView):

    def get_permissions(self):
        if self.request.method == 'POST':
            return [AllowAny()]
        return [IsAdminUser()]

    def post(self,request):
        serializer = UserSerializer(data= request.data)

        if serializer.is_valid():

            serializer.save()

            return Response({
                "user":serializer.data
            } , status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def get(self,request,pk=None):
        

        if pk:

            try:
                user = User.objects.get(pk = pk)
            except:
                return Response({
                    "message":"This user dosent exist"
                },status=status.HTTP_404_NOT_FOUND)

            serializer = UserSerializer(user)

            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            try:
                users = User.objects.all()
            except:
                return Response ({
                    "message":"cant get users,please try agan later"
                },status=status.HTTP_400_BAD_REQUEST)
            
            return Response(UserSerializer(users ,many=True).data,status=status.HTTP_200_OK)
            


class CustomTokenObtainPairView(TokenObtainPairView):

    def post(self, request, *args, **kwargs):
        response= super().post(request, *args, **kwargs)

        if response.status_code == 200:

            try:
                username= request.data.get('username')
                user = User.objects.get(username=username)
                user_data= UserSerializer(user).data
                response.data['user'] = user_data
            except:
                return Response({
                    "message": "User not found"
                },
                status=status.HTTP_401_UNAUTHORIZED
                )
        return response  
    

class LogoutView(APIView):
    permission_classes=[IsAuthenticated]

    def post (self,request):

        try:
            refresh_token = request.data.get('refresh_token')

            if not refresh_token :
                return Response (
                    {
                        "message": "Refresh token is required"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(
                {
                    "message":"User logged out successfully"
                },
                status= status.HTTP_200_OK
            )
        except Exception as e:
            return Response ({
                "message":str(e)
            },
            status=status.HTTP_400_BAD_REQUEST
            )
