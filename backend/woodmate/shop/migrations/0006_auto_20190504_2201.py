# Generated by Django 2.1.7 on 2019-05-04 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20190504_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='cid',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='shop.Customer'),
        ),
    ]
