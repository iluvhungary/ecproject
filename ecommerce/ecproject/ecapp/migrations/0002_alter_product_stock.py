# Generated by Django 4.2.9 on 2024-02-03 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.IntegerField(),
        ),
    ]
