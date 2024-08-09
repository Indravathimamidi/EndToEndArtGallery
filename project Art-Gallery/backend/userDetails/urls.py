from django.urls import path
from .views import Signin, Signup

urlpatterns=[
    path('Signup/', Signup, name='Signup'),
    path('Signin/', Signin, name='Signin'),
]