# Generated by Django 2.2.3 on 2020-04-05 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0036_answer_explanation'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='reference',
            field=models.TextField(null=True),
        ),
    ]
