# Generated by Django 4.1.4 on 2023-04-15 18:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('praind_chirho', '0003_alter_maquinariaequipochirho_modelo_chirho_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maquinariaequipochirho',
            name='id_chirho',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
