# Generated by Django 3.2.6 on 2022-11-11 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
