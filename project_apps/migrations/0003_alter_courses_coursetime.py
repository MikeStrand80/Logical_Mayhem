# Generated by Django 3.2.9 on 2021-12-05 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_apps', '0002_auto_20211205_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='courseTime',
            field=models.TimeField(),
        ),
    ]
