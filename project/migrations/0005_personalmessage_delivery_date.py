# Generated by Django 5.1.5 on 2025-04-29 16:20

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_alter_personalmessage_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalmessage',
            name='delivery_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
