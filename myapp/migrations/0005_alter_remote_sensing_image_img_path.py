# Generated by Django 5.1.4 on 2024-12-21 01:57

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0004_alter_remote_sensing_image_img_path"),
    ]

    operations = [
        migrations.AlterField(
            model_name="remote_sensing_image",
            name="img_path",
            field=models.ImageField(
                default=django.utils.timezone.now,
                max_length=128,
                upload_to="remote_sensing_images/",
                verbose_name="原始图像路径",
            ),
            preserve_default=False,
        ),
    ]
