# Generated by Django 5.1 on 2024-10-01 08:09

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('URL_SHORTNER_APP', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='url',
            old_name='long_url',
            new_name='original_url',
        ),
        migrations.AddField(
            model_name='url',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='url',
            name='short_url',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
