# Generated by Django 4.1 on 2022-08-05 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_remove_hoarding_images_hoarding_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='img_name',
            field=models.CharField(max_length=32),
        ),
    ]
