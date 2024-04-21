from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='/')
def hod(request):
    return render(request,'Hod/home.html')

@login_required(login_url='/')
def Add_student(request):
    return render(request,'Hod/add-student.html')