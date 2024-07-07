import sys
from django.contrib import messages
from django.db.models.signals import post_save
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.db.models import Q
from django.contrib.auth.models import User
from myapp.models import AccountUser, Course, AttendingCourse
from myapp.signals import check_nim
from myapp.forms import StudentRegisterForm

def readStudent(request):
    data = AccountUser.objects.all()
    context = {'data_list': data}
    return render(request, 'index.html', context)

@csrf_protect
def createStudent(request):
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            account_user = AccountUser(
                account_user_fullname=form.cleaned_data.get("fullname"),
                account_user_student_number=form.cleaned_data.get("nim"),
                account_user_email=form.cleaned_data.get("email"),  # perbaikan di sini
                account_user_created_by=request.user.username,
            )
            account_user.save()

            messages.success(request, 'Data Berhasil disimpan')
            return redirect('myapp:read-data-student')
    else:
        form = StudentRegisterForm()

    return render(request, 'form.html', {'form': form})

@csrf_protect
def updateStudent(request, id):
    student =  student.Object.AccountUser(account_user_id=id)  # perbaikan di sini

    if request.method == 'POST':
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            student.account_user_fullname = form.cleaned_data.get("fullname")
            student.account_user_student_number = form.cleaned_data.get("nim")
            student.account_user_email = form.cleaned_data.get("email")  # perbaikan di sini
            student.account_user_updated_by = request.user.username
            student.save()

            messages.success(request, 'Data Berhasil diupdate')
            return redirect('myapp:read-data-student')
    else:
        form = StudentRegisterForm(initial={
            'fullname': student.account_user_fullname,
            'nim': student.account_user_student_number,
            'email': student.account_user_email,  # perbaikan di sini
        })

    return render(request, 'update.html', {'form': form})

@csrf_protect
def deleteStudent(request, id):
    student = student.Object.AccountUser(account_user_id=id)  # perbaikan di sini
    student.delete()
    messages.success(request, 'Data Berhasil dihapus')
    return redirect('myapp:read-data-student')


def readCourse(request):
    data = Course.objects.all()[:1] #limit data (1 pcs)    context = {'data_list': data}
    return render(request, 'course.html', context)

@csrf_protect
def createCourse(request):
    return render(request, 'index.html')

@csrf_protect
def updateCourse(request):
    return render(request, 'index.html')

@csrf_protect
def deleteCourse(request, id):
    try:
        course = course.Objects.filter(username=id)
        course.delete()
        messages.success(request, 'Data Berhasil dihapus')
    except:
        messages.error(request, 'Data Tidak ditemukan')
    
    return redirect('myapp:read-data-course')

def home(request):
    return render(request, 'home.html')