# Generated by Django 2.2.24 on 2021-11-30 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0018_auto_20211130_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
