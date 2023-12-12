# Generated by Django 5.0 on 2023-12-12 16:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cardb",
            name="adv_month",
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="cardb",
            name="adv_year",
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="cardb",
            name="door_num",
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="cardb",
            name="engine_size",
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name="cardb",
            name="mileage",
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="cardb",
            name="price",
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="cardb",
            name="reg_year",
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="cardb",
            name="seat_num",
            field=models.IntegerField(null=True),
        ),
    ]