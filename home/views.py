from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from home.EmailBackEnd import EmailBackEnd
from django.contrib import messages
from django.contrib.auth.decorators import login_required


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



