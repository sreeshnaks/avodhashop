# Generated by Django 2.2 on 2022-08-09 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_auto_20220805_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
