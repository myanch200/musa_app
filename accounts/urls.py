from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('',views.home,name='home'),
    path('poem/<str:pk>/', views.poem_details,name='poem_details'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),

]