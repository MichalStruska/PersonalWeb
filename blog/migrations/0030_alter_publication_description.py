# Generated by Django 3.2.15 on 2022-08-22 21:38

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0029_auto_20220822_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
