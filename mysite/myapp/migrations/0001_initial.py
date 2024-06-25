# Generated by Django 5.0.6 on 2024-06-09 16:03

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountUser',
            fields=[
                ('account_user_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('account_user_related_user', models.CharField(max_length=255)),
                ('account_user_fullname', models.CharField(editable=False, max_length=255)),
                ('account_user_student_number', models.CharField(max_length=20)),
                ('account_user_created_by', models.CharField(max_length=255)),
                ('account_user_created_date', models.DateTimeField(auto_now_add=True)),
                ('account_user_updated_by', models.CharField(max_length=255, null=True)),
                ('account_user_updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('account_user_related_user',),
                'indexes': [models.Index(fields=['account_user_id', 'account_user_related_user'], name='myapp_accou_account_d6f119_idx')],
            },
        ),
    ]