# Generated by Django 4.1.2 on 2022-11-04 01:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0002_song'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='title',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Lyric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=1000)),
                ('song_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicapp.song')),
            ],
        ),
    ]