# Generated by Django 2.2.3 on 2020-04-06 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0037_question_reference'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='reference',
            new_name='reference_name',
        ),
        migrations.AddField(
            model_name='question',
            name='reference_link',
            field=models.URLField(null=True),
        ),
    ]