# Generated by Django 3.2.12 on 2023-05-01 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20230430_2203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_superuser',
        ),
        migrations.AddField(
            model_name='user',
            name='admin',
            field=models.BooleanField(default=False, help_text='lorem', verbose_name='Admin status'),
        ),
        migrations.AddField(
            model_name='user',
            name='staff',
            field=models.BooleanField(default=False, help_text='lorem', verbose_name='Staff status'),
        ),
    ]
