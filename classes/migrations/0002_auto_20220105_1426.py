# Generated by Django 3.2.6 on 2022-01-05 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='created_by',
        ),
        migrations.AlterField(
            model_name='result',
            name='file',
            field=models.FileField(upload_to='classes/results/'),
        ),
    ]
