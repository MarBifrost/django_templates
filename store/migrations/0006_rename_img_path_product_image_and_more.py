# Generated by Django 5.1.2 on 2024-10-23 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_product_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='img_path',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='product_name',
        ),
    ]
