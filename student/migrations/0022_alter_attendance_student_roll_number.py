# Generated by Django 4.1.3 on 2023-06-19 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0021_alter_attendance_student_roll_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='student_roll_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student'),
        ),
    ]