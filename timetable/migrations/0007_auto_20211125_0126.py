# Generated by Django 2.2.24 on 2021-11-24 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0006_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='lesson',
        ),
        migrations.AddField(
            model_name='teacher',
            name='lesson',
            field=models.ManyToManyField(to='timetable.Subject'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]