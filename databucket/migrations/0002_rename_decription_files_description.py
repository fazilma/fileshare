# Generated by Django 4.0.2 on 2022-02-28 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('databucket', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='files',
            old_name='decription',
            new_name='description',
        ),
    ]
