# Generated by Django 4.1.3 on 2023-06-24 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0049_branchsubjects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branchsubjects',
            name='year',
            field=models.TextField(choices=[('1st Year', '1st Year'), ('2nd Year', '2nd Year'), ('3rd Year', '3rd Year'), ('4th Year', '4th Year')]),
        ),
    ]
