# Generated by Django 4.1.3 on 2023-06-26 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0054_studentmarks_subject_1_result_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmarks',
            name='subject_1_result',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='studentmarks',
            name='subject_2_result',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='studentmarks',
            name='subject_3_result',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='studentmarks',
            name='subject_4_result',
            field=models.BooleanField(),
        ),
    ]
