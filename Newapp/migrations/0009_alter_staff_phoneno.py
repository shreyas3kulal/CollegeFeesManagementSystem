# Generated by Django 3.2.3 on 2021-06-02 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Newapp', '0008_alter_staff_phoneno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='PhoneNo',
            field=models.IntegerField(),
        ),
    ]