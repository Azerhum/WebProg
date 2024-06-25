from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import HttpResponse
from django.contrib.auth.models import User
from myapp.models import AccountUser

@receiver(post_save, sender=AccountUser, dispatch_uid="nim")
def check_nim(sender, instance, created, **kwargs):
    if created:
        get_student_number = AccountUser.objects.filter(account_user_student_number=instance.account_user_student_number)
        if get_student_number.exists():
            return HttpResponse('Data Exist')

        get_email = User.objects.filter(username=instance.account_user_related_user)
        if get_email.exists():
            return HttpResponse('Data Exist')

        User.objects.create(
            username=instance.account_user_related_user,
            email=instance.account_user_related_user
        )
        AccountUser.objects.create(
            account_user_related_user=instance.account_user_related_user,
            account_user_fullname=instance.account_user_fullname,
            account_user_student_number=instance.account_user_student_number
        )
