# Generated by Django 5.0.6 on 2024-06-23 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_remove_accountuser_myapp_accou_account_d6f119_idx_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountuser',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
