# Generated by Django 4.1.3 on 2023-06-24 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0048_delete_branchsubjects'),
    ]

    operations = [
        migrations.CreateModel(
            name='BranchSubjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.TextField(max_length=10)),
                ('subject_1', models.TextField(max_length=50)),
                ('subject_2', models.TextField(max_length=50)),
                ('subject_3', models.TextField(max_length=50)),
                ('subject_4', models.TextField(max_length=50)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.branch')),
            ],
        ),
    ]
