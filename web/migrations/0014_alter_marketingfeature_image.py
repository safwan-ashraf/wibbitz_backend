# Generated by Django 3.2.9 on 2021-11-24 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0013_auto_20211124_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marketingfeature',
            name='image',
            field=models.FileField(upload_to='marketings/'),
        ),
    ]
