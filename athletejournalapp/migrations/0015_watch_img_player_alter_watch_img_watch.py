# Generated by Django 4.1.6 on 2023-07-01 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('athletejournalapp', '0014_watch'),
    ]

    operations = [
        migrations.AddField(
            model_name='watch',
            name='img_player',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='watch',
            name='img_watch',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]