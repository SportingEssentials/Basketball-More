# Generated by Django 4.2.2 on 2023-06-21 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('athletejournalapp', '0004_rename_colonge_scent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scent',
            name='colonge_image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='scent',
            name='player_image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
