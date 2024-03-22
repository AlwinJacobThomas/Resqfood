from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User,FoodRequest
from rest_framework import authentication, permissions
# Create your views here.

class ListFoodRequest(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    ser
    def get(self,request):

        foodreq = FoodRequest.objects.all()
        return Response()

