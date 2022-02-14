# Generated by Django 4.0.1 on 2022-02-07 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_rename_patron1_unique_patron_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='unique',
            old_name='patron',
            new_name='patron1',
        ),
        migrations.RenameField(
            model_name='unique',
            old_name='patron_description',
            new_name='patron1_description',
        ),
        migrations.RenameField(
            model_name='unique',
            old_name='patron_name',
            new_name='patron1_name',
        ),
        migrations.RenameField(
            model_name='unique',
            old_name='patron_role',
            new_name='patron1_role',
        ),
        migrations.AddField(
            model_name='unique',
            name='patron2',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='unique',
            name='patron2_description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='unique',
            name='patron2_name',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='unique',
            name='patron2_role',
            field=models.CharField(default=11, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='unique',
            name='patron3',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='unique',
            name='patron3_description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='unique',
            name='patron3_name',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='unique',
            name='patron3_role',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
