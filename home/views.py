from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from home.EmailBackEnd import EmailBackEnd
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from home.models import CustomUser


# Create your views here.
def home(request):
    return render(request,'login.html')

def dologin(request):
    if request.method == "POST":
        user = EmailBackEnd.authenticate(request,username=request.POST.get('email'),password=request.POST.get('password'))
        if user != None:
            login(request, user)
            user_type = user.user_type
            if user_type == '1':
                # return HttpResponse("HOd Login")
                return redirect("/hod/home")
            elif user_type == '2':
                return HttpResponse("student")
            elif user_type == '3':
                return HttpResponse("teacher")
            else:
              messages.error(request,"username and password invalid")
              return redirect("/")
        else:
            messages.error(request, "username and password invalid")
            return redirect("/")

def dologout(request):
    logout(request)
    return redirect("/")

def profile(request):

    views = {}
    views['users'] = CustomUser.objects.get(id=request.user.id)
    return render(request,'profile.html',views)

@login_required(login_url='/')
def PROFILE_UPDATE(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        #email = request.POST.get('email')
        #username = request.POST.get('username')
        password = request.POST.get('password')
        print(profile_pic)
        try:
            customuser = CustomUser.objects.get(id = request.user.id)

            customuser.first_name = first_name
            customuser.last_name = last_name

            if password !=None and password != "":
                customuser.set_password(password)
            if profile_pic !=None and profile_pic != "":
                customuser.profile_pic = profile_pic
            customuser.save()
            messages.success(request,'Your Profile Updated Successfully !')
            return redirect('/profile')
        except:
            messages.error(request,'Failed To Update Your Profile')

    return render(request,'profile.html')



