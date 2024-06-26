# Generated by Django 5.0.4 on 2024-04-15 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0004_alter_profile_identity_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], default='Male', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='identity_type',
            field=models.CharField(blank=True, choices=[('Driver Licence', 'Driver Licence'), ('International Passport', 'International Passport'), ('National Identification Number', 'National Identification Number')], max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], default='Male', max_length=100),
        ),
    ]
