# Generated by Django 2.1.3 on 2018-12-18 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20181103_0512'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionuserdata',
            name='feedback',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
