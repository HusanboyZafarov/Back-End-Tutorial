# Generated by Django 3.2.6 on 2022-11-10 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20221110_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(upload_to='Blog_Images/%Y-Year/%m-Month'),
        ),
    ]
