# Generated by Django 5.0.6 on 2024-06-14 09:07

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_delete_student_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountuser',
            name='account_user_id',
            field=models.UUIDField(default=uuid.UUID('dfff0fb4-9167-45c2-85d9-61ea3460aa09'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]