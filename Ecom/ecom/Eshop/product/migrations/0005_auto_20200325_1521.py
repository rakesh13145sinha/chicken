# Generated by Django 3.0.3 on 2020-03-25 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0001_initial'),
        ('product', '0004_slider'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pieces',
            field=models.IntegerField(default=False),
        ),
        migrations.AddField(
            model_name='productimage',
            name='restaurant',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='Restaurant.Restaurants'),
        ),
    ]
