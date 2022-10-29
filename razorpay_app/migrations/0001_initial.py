# Generated by Django 4.1 on 2022-08-06 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Home', '0004_alter_image_img_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Create_payment_link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(blank=True, max_length=32, null=True)),
                ('user_contact', models.CharField(blank=True, max_length=32, null=True)),
                ('user_email', models.CharField(blank=True, max_length=32, null=True)),
                ('Amount', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(max_length=300)),
                ('status', models.CharField(choices=[('Paid', 'Paid'), ('Pending', 'Pending'), ('Failed', 'Failed')], default='Pending', max_length=32)),
                ('short_url', models.URLField()),
                ('payment_link_id', models.CharField(max_length=32)),
                ('payment_link_status', models.CharField(max_length=32)),
                ('razorpay_payment_id', models.CharField(max_length=32)),
                ('razorpay_signature', models.CharField(max_length=32)),
                ('Hoarding_id', models.ManyToManyField(to='Home.hoarding')),
            ],
        ),
    ]