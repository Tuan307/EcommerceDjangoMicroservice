# Generated by Django 4.1.7 on 2023-06-07 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_book_product_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='product_id',
        ),
    ]