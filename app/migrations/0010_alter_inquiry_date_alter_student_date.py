# Generated by Django 4.2.9 on 2024-07-13 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_student_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquiry',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
