# Generated by Django 4.0.1 on 2022-05-11 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='url',
            name='link',
        ),
        migrations.RemoveField(
            model_name='url',
            name='uuid',
        ),
        migrations.AddField(
            model_name='url',
            name='fullurl',
            field=models.CharField(default=3, max_length=1000, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='url',
            name='shorturl',
            field=models.CharField(default=3, max_length=10, unique=True),
            preserve_default=False,
        ),
    ]