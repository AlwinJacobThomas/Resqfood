from django.urls import path,include
from rest_framework import routers

# REST API routes 
router = routers.DefaultRouter() 

app_name ='collectApp'

urlpatterns = [
    # path('', index.views,name='index'),
    path('api/', include(router.urls)),
    
]