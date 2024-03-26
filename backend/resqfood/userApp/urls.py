from django.urls import path,include

from knox import views as knox_views
from .views import user_registration,user_login,change_password
# REST API routes 


app_name ='userApp'

urlpatterns = [
    # path('', index.views,name='index'),
   
    path('register/',user_registration ,name='register'),
    path('login/', user_login, name='login'),
    path('logout/',knox_views.LogoutView.as_view(),name='logout'),
    path('logoutall/',knox_views.LogoutAllView.as_view(),name='logout-all'),  #logout from all browsers
    path('changepassword/',change_password,name='change-password')
    # path('logout/', user_logout, name='logout'),
]