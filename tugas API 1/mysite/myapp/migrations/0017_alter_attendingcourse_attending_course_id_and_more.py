# Generated by Django 5.0.6 on 2024-07-07 04:07

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_course_attendingcourse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendingcourse',
            name='attending_course_id',
            field=models.UUIDField(default=uuid.UUID('472ee291-b883-484d-b8cb-9e85556ab0fc'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_id',
            field=models.UUIDField(default=uuid.UUID('6c28a74f-6d98-470e-bdcc-88426b6cad31'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]