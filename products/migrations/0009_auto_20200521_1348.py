# Generated by Django 3.0.6 on 2020-05-21 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20200521_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(default=1, upload_to='media/images/'),
            preserve_default=False,
        ),
    ]