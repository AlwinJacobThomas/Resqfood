
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from .serializers import UserSerializer,UserRegistrationSerializer


from knox.models import AuthToken
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
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
