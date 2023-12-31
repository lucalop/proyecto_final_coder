# Generated by Django 4.2.7 on 2023-12-13 00:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0009_alter_trekking_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='creation_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='comments',
            name='trekking',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='AppCoder.trekking'),
        ),
    ]
