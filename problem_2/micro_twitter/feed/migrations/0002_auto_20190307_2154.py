# Generated by Django 2.0.13 on 2019-03-07 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='followmodel',
            table='feed_follow',
        ),
        migrations.AlterModelTable(
            name='tweetmodel',
            table='feed_tweet',
        ),
    ]