# Generated by Django 4.1.7 on 2023-04-19 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0002_alter_song_files_options_alter_songs_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='song_files',
        ),
        migrations.DeleteModel(
            name='songs',
        ),
    ]
