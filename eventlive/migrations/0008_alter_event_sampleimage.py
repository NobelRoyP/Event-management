# Generated by Django 5.1.2 on 2024-12-16 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventlive', '0007_booking_event_feedback_alter_regester_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='sampleimage',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
    ]
