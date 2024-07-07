from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from myapp.models import AccountUser
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
                account_user_related_user=form.cleaned_data.get("email")
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
            student.account_user_related_user = form.cleaned_data.get("email")
            student.account_user_updated_by = request.user.username
            student.save()

            messages.success(request, 'Data Berhasil diupdate')
            return redirect('myapp:read-data-student')
    else:
        form = StudentRegisterForm(initial={
            'fullname': student.account_user_fullname,
            'nim': student.account_user_student_number,
            'email': student.account_user_related_user,
        })

    return render(request, 'update.html', {'form': form})

@csrf_protect
def deleteStudent(request, id):
    student = get_object_or_404(AccountUser, account_user_related_user=id)
    user = student.related_user 
    student.delete()
    user.delete()
    messages.success(request, 'Data Berhasil dihapus')
    return redirect('myapp:read-data-student')
