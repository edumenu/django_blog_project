# Generated by Django 2.2.1 on 2019-10-05 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20191005_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_img',
            field=models.ImageField(default='default.jpg', upload_to='images/'),
        ),
    ]
