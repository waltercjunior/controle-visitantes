# Generated by Django 3.0 on 2023-01-29 00:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='is_staf',
            new_name='is_staff',
        ),
    ]
