from django.contrib.auth import login,logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,permissions,generics #generics for change pswd

from rest_framework.authtoken.serializers import AuthTokenSerializer #Authentication Token
from .models import User
from .serializers import UserRegistrationSerializer,ChangePasswordSerializer
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView

# Create your views here.


class UserRegistration(APIView):    
    serializer_class = UserRegistrationSerializer
    
    def post(self,request,*args, **kwargs):    
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = AuthToken.objects.create(user)
            return Response({
                'user' : UserRegistrationSerializer(user,context = self.serializer_class()).data,
                'token' : token[1] 
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
user_registration = UserRegistration.as_view()

class UserLogin(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    
    def post(self,request,format=None):
        
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request,user)
        return super(UserLogin,self).post(request,format=None)
user_login = UserLogin.as_view()

class ChangePassword(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (permissions.IsAuthenticated,)
    
    def get_object(self,querset=None):
        obj =self.request.user
        return obj
    
    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            #check old pswd
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password":["Wrong Password,"]},status=status.HTTP_400_BAD_REQUEST)
            #set new pswd
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code':status.HTTP_200_OK,
                'message':'Password updated Sucessfully',
                'data':[]
            }
            return Response(response)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
            
change_password = ChangePassword.as_view()      