# Generated by Django 4.2.7 on 2023-12-12 23:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0005_remove_trekking_creation_date_alter_trekking_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trekking',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 12, 12, 20, 13, 16, 35647)),
        ),
    ]
