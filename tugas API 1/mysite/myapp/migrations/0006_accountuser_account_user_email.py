# Generated by Django 5.0.6 on 2024-06-23 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_rename_myapp_accou_account_5d0f2f_idx_myapp_accou_account_d6f119_idx_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountuser',
            name='account_user_email',
            field=models.EmailField(default='', max_length=255),
        ),
    ]
