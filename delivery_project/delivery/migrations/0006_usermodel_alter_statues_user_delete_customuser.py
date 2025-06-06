# Generated by Django 5.1.6 on 2025-04-05 22:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0005_customuser_delete_login_alter_statues_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='statues',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delivery.usermodel'),
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
