# Generated by Django 3.1.3 on 2021-05-25 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Newapp', '0002_auto_20210110_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='DateOfBirth',
            field=models.DateField(max_length=30),
        ),
        migrations.AlterField(
            model_name='staff',
            name='Email',
            field=models.EmailField(max_length=30),
        ),
        migrations.AlterField(
            model_name='staff',
            name='PinCode',
            field=models.IntegerField(max_length=30),
        ),
        migrations.AlterField(
            model_name='staff',
            name='Salary',
            field=models.IntegerField(max_length=30),
        ),
    ]
