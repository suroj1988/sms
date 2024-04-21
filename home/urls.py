from .views import *
from .hodviews import *
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    path('login', dologin, name='dologin'),
    path('logout', dologout, name='dologout'),
    path('hod/home', hod, name='hod/home'),
    path('profile', profile, name='profile'),
    path('profile/update',PROFILE_UPDATE, name='profile_update'),
    path('add_student',Add_student, name='add_student'),



]