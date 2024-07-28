# Generated by Django 5.0.6 on 2024-07-28 09:25

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('street', models.CharField(max_length=255)),
                ('suite', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('zipcode', models.CharField(max_length=10)),
                ('geo_lat', models.CharField(max_length=50)),
                ('geo_lng', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('website', models.URLField()),
                ('company_name', models.CharField(max_length=255)),
                ('company_catchPhrase', models.CharField(max_length=255)),
                ('company_bs', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='AccountUser',
            fields=[
                ('account_user_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('account_user_related_user', models.CharField(editable=False, max_length=255)),
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
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('course_name', models.CharField(editable=False, max_length=255)),
                ('course_created_by', models.CharField(max_length=255)),
                ('course_created_date', models.DateTimeField(auto_now_add=True)),
                ('course_updated_by', models.CharField(max_length=255, null=True)),
                ('course_updated_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('course_id',),
                'indexes': [models.Index(fields=['course_id'], name='myapp_cours_course__4e3bc2_idx')],
            },
        ),
        migrations.CreateModel(
            name='AttendingCourse',
            fields=[
                ('attending_course_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('attending_account_profile_id', models.CharField(editable=False, max_length=255)),
                ('attending_course_created_by', models.CharField(max_length=255)),
                ('attending_course_created_date', models.DateTimeField(auto_now_add=True)),
                ('attending_course_updated_by', models.CharField(max_length=255, null=True)),
                ('attending_course_updated_date', models.DateTimeField(auto_now_add=True)),
                ('attending_courseid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.course')),
            ],
            options={
                'ordering': ('attending_course_id',),
                'indexes': [models.Index(fields=['attending_course_id', 'attending_courseid'], name='myapp_atten_attendi_66ed4b_idx')],
            },
        ),
    ]
