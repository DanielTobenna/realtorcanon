# Generated by Django 3.2 on 2024-05-15 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtorcanonapp', '0002_auto_20240515_0852'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
