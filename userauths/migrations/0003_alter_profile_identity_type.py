# Generated by Django 5.0.4 on 2024-04-15 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0002_alter_user_gender_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='identity_type',
            field=models.CharField(blank=True, choices=[('Driver Licence', 'Driver Licence'), ('National Identification Number', 'National Identification Number'), ('International Passport', 'International Passport')], max_length=150, null=True),
        ),
    ]
