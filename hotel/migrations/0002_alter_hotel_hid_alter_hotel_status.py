# Generated by Django 5.0.4 on 2024-04-15 22:12

import shortuuid.django_fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='hid',
            field=shortuuid.django_fields.ShortUUIDField(alphabet='0123456789', length=5, max_length=7, prefix='HOTEL', unique=True),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='status',
            field=models.CharField(choices=[('Disable', 'Disable'), ('In review', 'In review'), ('Rejected', 'Rejected'), ('Draft', 'Draft'), ('Live', 'Live')], default='Live', max_length=20),
        ),
    ]
