# Generated by Django 4.1.13 on 2023-11-19 22:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bookcatalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
