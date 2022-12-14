# Generated by Django 2.2 on 2022-08-05 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='cart',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='cart.cartlist'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='items',
            name='prodt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.products'),
        ),
    ]
