# Generated by Django 3.2.9 on 2021-12-06 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_apps', '0004_courses_coursenum'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='phoneNum',
            field=models.CharField(default=0, max_length=15),
        ),
    ]
