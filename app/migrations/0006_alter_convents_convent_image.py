# Generated by Django 4.0.1 on 2022-04-06 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_rename_image_convents_convent_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convents',
            name='convent_image',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
