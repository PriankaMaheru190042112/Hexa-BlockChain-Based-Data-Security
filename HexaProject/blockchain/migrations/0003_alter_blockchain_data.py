# Generated by Django 4.2.3 on 2023-07-18 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blockchain", "0002_alter_blockchain_data_delete_block"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blockchain",
            name="data",
            field=models.CharField(max_length=255),
        ),
    ]