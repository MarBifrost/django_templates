# Generated by Django 5.1.2 on 2024-10-23 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_rename_img_path_product_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='df_image.png', max_length=255, upload_to='img/', verbose_name='image'),
        ),
    ]