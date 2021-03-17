from django.urls import path
from .views import *

app_name = 'users'
urlpatterns = [
    path('', SignUp.as_view(), name='sign_up'),
    path('sign_in/', SignIn.as_view(), name='sign_in'),
    path('sign_out', SignOut.as_view(), name='sign_out'),
    path('success/', success, name='success'),
    path('password_reset/', PasswordReset.as_view(), name='password_reset'),
    path('password_done/', PasswordResetDone.as_view(), name='password_done'),
    path('password_confirm/<uidb64>/<token>/', PasswordResetConfirm.as_view(), name='password_confirm'),
    path('password_complete/', PasswordResetComplete.as_view(), name='password_complete'),
]
