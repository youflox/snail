# Generated by Django 4.0.2 on 2022-02-06 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_upload', '0002_rename_user_id_file_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='data_uploaded',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]