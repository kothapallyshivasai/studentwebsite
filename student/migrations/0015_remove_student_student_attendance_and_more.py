# Generated by Django 4.1.3 on 2023-06-19 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0014_student_student_address_alter_student_student_branch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='student_attendance',
        ),
        migrations.AlterField(
            model_name='student',
            name='student_address',
            field=models.TextField(max_length=200),
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('january_attendance', models.IntegerField(default=100)),
                ('febraury_attendance', models.IntegerField(default=100)),
                ('march_attendance', models.IntegerField(default=100)),
                ('april_attendance', models.IntegerField(default=100)),
                ('may_attendance', models.IntegerField(default=100)),
                ('june_attendance', models.IntegerField(default=100)),
                ('july_attendance', models.IntegerField(default=100)),
                ('august_attendance', models.IntegerField(default=100)),
                ('september_attendance', models.IntegerField(default=100)),
                ('october_attendance', models.IntegerField(default=100)),
                ('november_attendance', models.IntegerField(default=100)),
                ('december_attendance', models.IntegerField(default=100)),
                ('student_roll_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
    ]
