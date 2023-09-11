# Generated by Django 4.1.3 on 2023-06-26 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0053_rename_subject1_studentmarks_subject_1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentmarks',
            name='subject_1_result',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='studentmarks',
            name='subject_2_result',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='studentmarks',
            name='subject_3_result',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='studentmarks',
            name='subject_4_result',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='BranchDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.branch')),
            ],
        ),
    ]
