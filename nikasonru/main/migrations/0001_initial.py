# Generated by Django 3.2.6 on 2022-12-04 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BeforeAfter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_before', models.ImageField(upload_to='Before_images/%Y-Year/%m-Month')),
                ('image_after', models.ImageField(upload_to='After_images/%Y-Year/%m-Month')),
            ],
        ),
        migrations.CreateModel(
            name='ClientsAboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Clients_About_Us/%Y-Year/%m-Month')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='Users_Message/%Y-Year/%m-Month')),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Portfolio/%Y-Year/%m-Month')),
            ],
        ),
        migrations.CreateModel(
            name='SmiAboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Smi_about_us/%Y-Year/%m-Month')),
            ],
        ),
    ]
