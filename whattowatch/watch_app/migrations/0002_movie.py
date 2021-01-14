# Generated by Django 3.1.4 on 2021-01-14 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watch_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('rotten_tomatos', models.FloatField(blank=True)),
                ('hulu_url', models.CharField(blank=True, max_length=100)),
                ('amazon_url', models.CharField(blank=True, max_length=100)),
                ('hbo_max_url', models.CharField(blank=True, max_length=100)),
                ('netflix_url', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
