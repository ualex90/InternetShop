# Generated by Django 4.2.5 on 2023-10-28 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_rename_created_by_user_product_producer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='producer',
            new_name='owner',
        ),
    ]
