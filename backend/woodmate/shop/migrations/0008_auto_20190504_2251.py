# Generated by Django 2.1.7 on 2019-05-04 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_product_product_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_pic',
            field=models.ImageField(blank=True, null=True, upload_to='picture'),
        ),
    ]
