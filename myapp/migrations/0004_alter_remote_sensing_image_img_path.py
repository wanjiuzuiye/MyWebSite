# Generated by Django 5.1.4 on 2024-12-21 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0003_alter_augment_image_img_path_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="remote_sensing_image",
            name="img_path",
            field=models.ImageField(
                blank=True,
                max_length=128,
                null=True,
                upload_to="remote_sensing_images/",
                verbose_name="原始图像路径",
            ),
        ),
    ]