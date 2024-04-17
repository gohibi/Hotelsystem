# Generated by Django 5.0.4 on 2024-04-17 12:25

import shortuuid.django_fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0011_alter_booking_status_payment_alter_hotel_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='status_payment',
            field=models.CharField(choices=[('expired', 'Expired'), ('failed', 'Failed'), ('unpaid', 'Unpaid'), ('refunded', 'refunded'), ('pending', 'Pending'), ('processing', 'Processing'), ('cancelled', 'Cancelled'), ('refunding', 'Refunding'), ('initiated', 'Initiated'), ('paid', 'Paid')], max_length=100),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='status',
            field=models.CharField(choices=[('Live', 'Live'), ('In review', 'In review'), ('Rejected', 'Rejected'), ('Disable', 'Disable'), ('Draft', 'Draft')], default='Live', max_length=20),
        ),
        migrations.AlterField(
            model_name='hotelfeatures',
            name='icontype',
            field=models.CharField(blank=True, choices=[('Box icons', 'Box icons'), ('Bootstrap icons', 'Bootstrap icons'), ('Remi icons', 'Remi icons'), ('Fontawesome icons', 'Fontawesome icons'), ('Flat icons', 'Flat icons')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='rid',
            field=shortuuid.django_fields.ShortUUIDField(alphabet='0123456789', length=6, max_length=8, prefix='ROOM', unique=True),
        ),
    ]
