# Generated by Django 5.1.5 on 2025-04-16 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalmessage',
            name='max_delivery',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='personalmessage',
            name='min_delivery',
            field=models.DateTimeField(),
        ),
    ]
