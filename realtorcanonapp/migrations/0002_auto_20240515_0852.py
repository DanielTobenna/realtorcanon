# Generated by Django 3.2 on 2024-05-15 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realtorcanonapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='description',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.RemoveField(
            model_name='property',
            name='features',
        ),
        migrations.AddField(
            model_name='property',
            name='features',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='realtorcanonapp.propertyfeature'),
        ),
        migrations.AlterField(
            model_name='property',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='propertyimage',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
