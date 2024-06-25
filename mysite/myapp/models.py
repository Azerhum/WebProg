from django.db import models
from django.utils.html import escape
from django.utils.safestring import mark_safe
import uuid

class AccountUser(models.Model):
    account_user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    account_user_related_user = models.CharField(max_length=255, null=False, editable=False)
    account_user_fullname = models.CharField(max_length=255, null=False)
    account_user_student_number = models.CharField(max_length=20, null=False)
    account_user_email = models.EmailField(null=False)
    account_user_created_by = models.CharField(max_length=255, null=False)
    account_user_created_date = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    account_user_updated_by = models.CharField(max_length=255, null=True)
    account_user_updated_date = models.DateTimeField(editable=False, null=False, auto_now=True)

    def __str__(self):
        return self.account_user_related_user

    @property
    def friendly_profile(self):
        return mark_safe(
            f"{escape(self.account_user_id)} &lt;{escape(self.account_user_related_user)}&gt;<br/>"
            f"Full Name: {escape(self.account_user_fullname)}<br/>"
            f"Student Number: {escape(self.account_user_student_number)}<br/>"
            f"Created By: {escape(self.account_user_created_by)}<br/>"
            f"Created Date: {escape(self.account_user_created_date)}<br/>"
            f"Updated By: {escape(self.account_user_updated_by)}<br/>"
            f"Updated Date: {escape(self.account_user_updated_date)}"
        )

    class Meta:
        ordering = ('account_user_related_user',)
        indexes = [
            models.Index(fields=['account_user_id']),
            models.Index(fields=['account_user_related_user']),
        ]
