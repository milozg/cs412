# Generated by Django 5.1.5 on 2025-03-31 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voter_analytics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='v20state',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='voter',
            name='v21primary',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='voter',
            name='v21town',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='voter',
            name='v22general',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='voter',
            name='v23town',
            field=models.TextField(),
        ),
    ]
