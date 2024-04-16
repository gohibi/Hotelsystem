# Generated by Django 5.0.4 on 2024-04-15 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0003_alter_profile_identity_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='identity_type',
            field=models.CharField(blank=True, choices=[('International Passport', 'International Passport'), ('National Identification Number', 'National Identification Number'), ('Driver Licence', 'Driver Licence')], max_length=150, null=True),
        ),
    ]