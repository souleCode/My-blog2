# Generated by Django 4.1.6 on 2023-04-07 18:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0003_comment"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("slug", models.SlugField(max_length=200)),
            ],
        ),
    ]
