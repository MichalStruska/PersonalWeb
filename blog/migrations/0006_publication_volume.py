# Generated by Django 2.0 on 2022-09-08 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20220907_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='volume',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
