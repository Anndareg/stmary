# Generated by Django 4.0.1 on 2022-03-02 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery_category',
            name='function_name',
            field=models.CharField(max_length=30),
        ),
    ]
