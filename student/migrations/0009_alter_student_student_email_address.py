# Generated by Django 4.1.3 on 2023-06-16 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_student_student_email_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_email_address',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
