# Generated by Django 3.2.3 on 2021-05-25 11:38

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('Newapp', '0007_auto_20210525_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='PhoneNo',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31),
        ),
    ]
