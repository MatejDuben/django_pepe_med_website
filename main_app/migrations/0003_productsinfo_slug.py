# Generated by Django 3.2.8 on 2021-11-01 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_remove_shopitem_is_ordered'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsinfo',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
