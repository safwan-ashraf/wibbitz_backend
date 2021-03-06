# Generated by Django 3.2.9 on 2021-11-26 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0020_alter_customer_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='hero_image',
            field=models.FileField(default='Studio', upload_to='products/hero_images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default='a', max_length=128),
            preserve_default=False,
        ),
    ]
