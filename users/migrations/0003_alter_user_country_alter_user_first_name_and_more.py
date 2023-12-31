# Generated by Django 4.2.5 on 2023-10-29 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_key_alter_user_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='country',
            field=models.CharField(blank=True, choices=[('BY', 'Беларусь'), ('KZ', 'Казахстан'), ('CK', 'Острова Кука'), ('LV', 'Латвия'), ('OS', 'Южная Осетия'), ('KG', 'Киргизия'), ('AM', 'Армения'), ('LT', 'Литва'), ('UZ', 'Узбекистан'), ('GE', 'Грузия'), ('RU', 'Россия'), ('MD', 'Молдова'), ('XX', 'Другая страна')], max_length=25, null=True, verbose_name='страна'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=35, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=35, null=True, verbose_name='Фамилия'),
        ),
    ]
