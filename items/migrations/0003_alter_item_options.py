# Generated by Django 5.0.2 on 2024-02-10 05:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("items", "0002_alter_category_options_item"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="item",
            options={
                "ordering": (
                    "name",
                    "category",
                    "price",
                    "is_sold",
                    "created_by",
                    "created_at",
                ),
                "verbose_name_plural": "Items",
            },
        ),
    ]
