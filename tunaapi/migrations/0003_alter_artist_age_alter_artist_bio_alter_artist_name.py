# Generated by Django 4.2.8 on 2024-12-11 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tunaapi', '0002_genre_songs_alter_genre_description_alter_song_album_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='artist',
            name='bio',
            field=models.TextField(max_length=150),
        ),
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(max_length=45),
        ),
    ]