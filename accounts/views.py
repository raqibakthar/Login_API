from rest_framework.response import Response
from rest_framework.views import APIView
from.serializers import RegisterSerializer,LoginSerializer
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class RegisterApi(APIView):

    def post(self,request):
        try:
            data = request.data
            serializer = RegisterSerializer(data=data)

            if not serializer.is_valid():

                return Response({
                    "data":{},
                    "message":"validation error"
                },status=status.HTTP_400_BAD_REQUEST)
            
            serializer.save()

            return Response({
                    "data":serializer.data,
                    "message":"you are registered successfully"
                },status=status.HTTP_201_CREATED)
        
        except Exception as e:

            return Response({
                    "data":{},
                    "message":"something went wrong"
                },status=status.HTTP_400_BAD_REQUEST)
    

class LoginApi(APIView):

    def post(self,request):
        try:
            data = request.data
            serializer = LoginSerializer(data=data)

            if not serializer.is_valid():

                return Response({
                    "data":{},
                    "message":"something went wrong"
                },status=status.HTTP_400_BAD_REQUEST)
            
            user = authenticate(username=serializer.data['username'],password=serializer.data['password'])

            if not user:
                return Response({
                    "data":{},
                    "message":"Invalid credentials"
                },status=status.HTTP_400_BAD_REQUEST)
            
            token,extra = Token.objects.get_or_create(user=user)

            return Response({
                "data":serializer.data,
                "token":str(token),
                "message":"Login successfull"
            },status=status.HTTP_200_OK)
        
        except Exception as e:
            print(e)
            return Response({
                    "data":{},
                    "message":"something went wrong"
                },status=status.HTTP_400_BAD_REQUEST)

class LogoutApi(APIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def post(self,request):

        try:    
            request.user.auth_token.delete()

            return Response({
                "data":{},
                "message":"logout successful",
            },status=status.HTTP_200_OK)
        
        except Exception as e:

            return Response({
                    "data":{},
                    "message":"something went wrong"
                },status=status.HTTP_400_BAD_REQUEST)

class HomeApi(APIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self,request):
        try:
            print(request.user)
            return Response({

                "message":"This is home page"

            },status=status.HTTP_202_ACCEPTED)
        
        except Exception as e:
          
            return Response({

                "message":"something went wrong"

            },status=status.HTTP_404_NOT_FOUND)