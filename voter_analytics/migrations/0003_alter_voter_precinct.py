# Generated by Django 5.1.5 on 2025-03-31 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voter_analytics', '0002_alter_voter_v20state_alter_voter_v21primary_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='precinct',
            field=models.TextField(),
        ),
    ]
