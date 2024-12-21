# Generated by Django 5.1.4 on 2024-12-21 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0005_alter_remote_sensing_image_img_path"),
    ]

    operations = [
        migrations.AddField(
            model_name="remote_sensing_image",
            name="img_name",
            field=models.CharField(
                default="noname", max_length=64, verbose_name="图像名称"
            ),
            preserve_default=False,
        ),
    ]