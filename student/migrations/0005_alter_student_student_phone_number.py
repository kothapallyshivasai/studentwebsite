# Generated by Django 4.1.3 on 2023-06-16 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_student_student_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_phone_number',
            field=models.IntegerField(unique=True),
        ),
    ]
