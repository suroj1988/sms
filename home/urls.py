from .views import *
from .hodviews import *
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    path('login', dologin, name='dologin'),
    path('logout', dologout, name='dologout'),
    path('hod/home', hod, name='hod/home'),


]