# Generated by Django 4.1.3 on 2023-06-26 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0057_alter_branchdetails_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branchdetails',
            name='description',
            field=models.CharField(default='Hello', max_length=300),
        ),
    ]
