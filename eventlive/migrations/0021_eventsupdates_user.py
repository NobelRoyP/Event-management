# Generated by Django 5.1.3 on 2025-02-01 09:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("eventlive", "0020_eventsupdates_stock"),
    ]

    operations = [
        migrations.AddField(
            model_name="eventsupdates",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="eventlive.organizer",
            ),
        ),
    ]
