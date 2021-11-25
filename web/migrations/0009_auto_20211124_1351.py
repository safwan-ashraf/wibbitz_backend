# Generated by Django 3.2.9 on 2021-11-24 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_testimonial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='icon',
            field=models.FileField(upload_to='features/icons/'),
        ),
        migrations.AlterField(
            model_name='feature',
            name='image',
            field=models.ImageField(upload_to='features/images/'),
        ),
    ]
