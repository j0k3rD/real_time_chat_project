# Generated by Django 3.2.12 on 2023-05-07 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('is_active', models.BooleanField(default=True, help_text='lorem', verbose_name='Active')),
                ('staff', models.BooleanField(default=False, help_text='lorem', verbose_name='Staff status')),
                ('admin', models.BooleanField(default=False, help_text='lorem', verbose_name='Admin status')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
