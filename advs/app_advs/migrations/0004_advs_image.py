# Generated by Django 4.0.10 on 2023-08-24 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_advs', '0003_advs_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='advs',
            name='image',
            field=models.ImageField(default='', upload_to='advs/', verbose_name='изображение'),
            preserve_default=False,
        ),
    ]
