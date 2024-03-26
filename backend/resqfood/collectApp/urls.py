from django.urls import path,include

from .views import UserRegistration
# REST API routes 


app_name ='collectApp'

urlpatterns = [
    # path('', index.views,name='index'),
   
    path('register/',UserRegistration.as_view(),name='register')
]