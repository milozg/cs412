# Generated by Django 5.1.5 on 2025-02-19 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField(blank=True)),
                ('last_name', models.TextField(blank=True)),
                ('city', models.TextField(blank=True)),
                ('email', models.TextField(blank=True)),
                ('image_url', models.URLField(blank=True)),
            ],
        ),
    ]
