# Generated by Django 5.0 on 2024-04-01 11:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_work', '0023_delete_userarea'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='my_work.area'),
        ),
    ]
