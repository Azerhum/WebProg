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

def home(request):
    return render(request, 'home.html')

def readCourse(request):
    data = Course.objects.all()[:1]  # Limit data (1 piece)
    context = {'data_list': data}
    return render(request, 'course.html', context)


@csrf_protect
def createCourse(request):
    return render(request, 'home.html')


@csrf_protect
def updateCourse(request):
    return render(request, 'home.html')


@csrf_protect
def deleteCourse(request):
    try:
        data = Course.objects.filter(course_id=id)
        if data:
            data.delete()
            messages.success(request, 'Data Berhasil dihapus')
            return redirect('myFirstApp:read-data-course')
        else:
            messages.success(request, 'Data Tidak ditemukan')
            return redirect('myFirstApp:read-data-course')
    except:
        return redirect('myFirstApp:read-data-course')

# Create your views here.
def readStudent(request):
    data = AccountUser.objects.all()
    context = {'data_list': data}
    return render(request, 'index.html', context)

@csrf_protect
def createStudent(request):
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            fullname = form.cleaned_data.get("fullname")
            nim = form.cleaned_data.get("nim")
            email = form.cleaned_data.get("email")
            
            # Create User first
            user = User.objects.create(username=email, email=email)

            # Create AccountUser
            account_user = AccountUser(
                account_user_fullname=fullname,
                account_user_student_number=nim,
                account_user_related_user=user.username,  # use username to link
                account_user_created_by=request.user.username
            )
            account_user.save()

            messages.success(request, 'Data Berhasil disimpan')
            return redirect('myapp:read-data-student')
    else:
        form = StudentRegisterForm()
    
    return render(request, 'form.html', {'form': form})

@csrf_protect
def updateStudent(request, id):
    student = AccountUser.objects.get(account_user_related_user=id)
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            student.account_user_fullname = form.cleaned_data.get("fullname")
            student.account_user_student_number = form.cleaned_data.get("nim")
            student.account_user_updated_by = request.user.username
            student.save()
            messages.success(request, 'Data Berhasil diupdate')
            return redirect('myapp:read-data-student')
    else:
        form = StudentRegisterForm(initial={
            'fullname': student.account_user_fullname,
            'nim': student.account_user_student_number,
        })
    return render(request, 'form.html', {'form': form})

@csrf_protect
def deleteStudent(request, id):
    try:
        member = AccountUser.objects.get(account_user_related_user=id)
        user = User.objects.get(username=member.account_user_related_user)
        member.delete()
        user.delete()
        messages.success(request, 'Data Berhasil dihapus')
    except AccountUser.DoesNotExist:
        messages.error(request, 'AccountUser tidak ditemukan')
    except User.DoesNotExist:
        messages.warning(request, 'User tidak ditemukan, hanya AccountUser yang dihapus')
        member.delete()
    return redirect('myapp:read-data-student')