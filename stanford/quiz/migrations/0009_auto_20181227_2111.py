# Generated by Django 2.1.3 on 2018-12-27 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0008_auto_20181227_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionmedia',
            name='media_type',
            field=models.CharField(choices=[('IMG', 'Image'), ('VID', 'Video'), ('AUD', 'Audio')], max_length=3),
        ),
    ]
