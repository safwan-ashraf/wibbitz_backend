# Generated by Django 3.2.9 on 2021-11-25 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0018_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='white_logo',
            field=models.FileField(blank=True, null=True, upload_to='customers/'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='company_size',
            field=models.CharField(choices=[('1', '1-10'), ('2', '11-50'), ('3', '51-200'), ('4', '201-500'), ('5', '501-100')], max_length=128),
        ),
        migrations.AlterField(
            model_name='contact',
            name='industry',
            field=models.CharField(choices=[('1', 'Agriculture'), ('2', 'Banking & Finance'), ('3', 'Business Services & Software'), ('4', 'Automobile')], max_length=128),
        ),
    ]
