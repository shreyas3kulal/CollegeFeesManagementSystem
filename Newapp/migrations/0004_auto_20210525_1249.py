# Generated by Django 3.1.3 on 2021-05-25 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Newapp', '0003_auto_20210525_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='DateOfBirth',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='staff',
            name='PinCode',
            field=models.IntegerField(max_length=6),
        ),
    ]