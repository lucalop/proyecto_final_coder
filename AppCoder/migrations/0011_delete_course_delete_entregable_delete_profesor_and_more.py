# Generated by Django 4.2.7 on 2023-12-14 00:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0010_alter_comments_creation_date_alter_comments_trekking'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Entregable',
        ),
        migrations.DeleteModel(
            name='Profesor',
        ),
        migrations.DeleteModel(
            name='Students',
        ),
    ]