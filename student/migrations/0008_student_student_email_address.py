# Generated by Django 4.1.3 on 2023-06-16 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_alter_student_student_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_email_address',
            field=models.EmailField(default='whatever123@gmail.com', max_length=254),
        ),
    ]
