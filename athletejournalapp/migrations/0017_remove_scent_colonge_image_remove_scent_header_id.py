# Generated by Django 4.1.6 on 2023-07-06 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('athletejournalapp', '0016_remove_basketballessential_comparison_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scent',
            name='colonge_image',
        ),
        migrations.RemoveField(
            model_name='scent',
            name='header_id',
        ),
    ]