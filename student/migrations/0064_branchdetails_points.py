# Generated by Django 4.1.3 on 2023-06-26 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0063_alter_attendance_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='branchdetails',
            name='points',
            field=models.TextField(default=''),
        ),
    ]
