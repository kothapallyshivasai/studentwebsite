# Generated by Django 4.1.3 on 2023-05-22 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_roll_number', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('student_password', models.CharField(max_length=100)),
                ('student_first_name', models.CharField(max_length=40)),
                ('student_last_name', models.CharField(max_length=40)),
                ('student_date_of_birth', models.DateField()),
                ('student_year', models.CharField(choices=[('1st Year', '1st Year'), ('2nd Year', '2nd Year'), ('3rd Year', '3rd Year'), ('4th Year', '4th Year')], max_length=100)),
                ('student_semester', models.CharField(choices=[('1', '1'), ('2', '2')], max_length=100)),
                ('student_picture', models.ImageField(upload_to='testimonials/')),
            ],
        ),
    ]
