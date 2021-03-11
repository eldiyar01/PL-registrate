from django.urls import path
from .views import *

app_name = 'users'
urlpatterns = [
    path('', SignUp.as_view(), name='sign_up'),
    path('success/', success, name='success'),
]
