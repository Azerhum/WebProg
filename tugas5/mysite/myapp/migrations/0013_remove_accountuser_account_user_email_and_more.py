# Generated by Django 5.0.6 on 2024-06-25 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_alter_accountuser_account_user_fullname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accountuser',
            name='account_user_email',
        ),
        migrations.AlterField(
            model_name='accountuser',
            name='account_user_fullname',
            field=models.CharField(editable=False, max_length=255),
        ),
    ]
