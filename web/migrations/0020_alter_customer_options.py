# Generated by Django 3.2.9 on 2021-11-26 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0019_auto_20211125_1535'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['-id']},
        ),
    ]
