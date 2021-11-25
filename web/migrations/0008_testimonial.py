# Generated by Django 3.2.9 on 2021-11-24 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_videoblog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='testimonials/')),
                ('logo', models.FileField(blank=True, null=True, upload_to='testimonials/')),
                ('description', models.TextField()),
                ('name', models.CharField(max_length=255)),
                ('designation', models.CharField(max_length=255)),
                ('company_name', models.CharField(max_length=128)),
                ('is_featured', models.BooleanField(default=False)),
            ],
        ),
    ]
