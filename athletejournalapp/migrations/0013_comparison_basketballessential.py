# Generated by Django 4.1.6 on 2023-06-27 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('athletejournalapp', '0012_scent_header_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comparison',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comp_name', models.CharField(max_length=200, null=True)),
                ('comp_url', models.URLField(max_length=500, null=True)),
                ('comp_img', models.ImageField(null=True, upload_to='images/')),
                ('comp_price_index', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='BasketballEssential',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
                ('coupons', models.CharField(blank=True, max_length=200)),
                ('benefits', models.CharField(blank=True, max_length=400)),
                ('stars', models.DecimalField(blank=True, decimal_places=2, max_digits=3)),
                ('brand', models.CharField(blank=True, max_length=200)),
                ('material', models.CharField(blank=True, max_length=200)),
                ('url', models.URLField()),
                ('sale', models.CharField(blank=True, max_length=100)),
                ('genre', models.CharField(blank=True, max_length=300)),
                ('comparison', models.ManyToManyField(blank=True, to='athletejournalapp.comparison')),
            ],
        ),
    ]
