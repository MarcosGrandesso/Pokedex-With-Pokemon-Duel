# Generated by Django 4.0.5 on 2023-02-07 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='img_url',
            field=models.CharField(blank=True, default=None, max_length=10000, null=True),
        ),
    ]
