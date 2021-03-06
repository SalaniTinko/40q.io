# Generated by Django 3.1 on 2021-01-10 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CropModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('bucket_name', models.CharField(max_length=30)),
                ('bucket_url', models.URLField()),
            ],
        ),
    ]
