# Generated by Django 3.2.3 on 2021-06-02 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Newapp', '0009_alter_staff_phoneno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='Address',
            field=models.CharField(max_length=50),
        ),
    ]
