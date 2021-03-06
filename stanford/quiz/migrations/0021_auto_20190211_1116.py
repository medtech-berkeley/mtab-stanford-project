# Generated by Django 2.1.3 on 2019-02-11 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0020_auto_20190211_0715'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='num',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='difficulty',
            field=models.CharField(choices=[('Basic', 'Basic'), ('Intermediate', 'Intermediate'), ('Expert', 'Expert')], default='Basic', max_length=20),
        ),
        migrations.AlterUniqueTogether(
            name='answer',
            unique_together={('num', 'question')},
        ),
    ]
