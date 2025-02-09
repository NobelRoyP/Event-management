# Generated by Django 5.0.4 on 2025-01-04 09:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventlive', '0014_alter_event_sampleimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='eventsupdates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=60, null=True)),
                ('eventname', models.CharField(blank=True, max_length=60, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='eventsimg/')),
                ('details', models.CharField(blank=True, max_length=300, null=True)),
                ('eventdate', models.DateField(blank=True, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('registerenddate', models.DateField(blank=True, null=True)),
                ('resultdate', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('approved', 'APPROVED'), ('pending', 'PENDING'), ('rejected', 'REJECTED')], default='pending', max_length=12)),
                ('msg', models.CharField(default='None', max_length=45)),
                ('staff_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='eventlive.regester')),
            ],
        ),
    ]
