# Generated by Django 4.0.1 on 2022-04-06 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_convents_convent_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convents',
            name='convent_image',
            field=models.FileField(blank=True, default=1, upload_to=''),
            preserve_default=False,
        ),
    ]