# Generated by Django 5.1.6 on 2025-04-05 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0003_login_last_login'),
    ]

    operations = [
        migrations.RenameField(
            model_name='login',
            old_name='email',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='login',
            name='last_login',
        ),
    ]
