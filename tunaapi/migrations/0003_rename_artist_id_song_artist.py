# Generated by Django 4.2.8 on 2024-12-04 02:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tunaapi', '0002_rename_desription_genre_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='artist_id',
            new_name='artist',
        ),
    ]
