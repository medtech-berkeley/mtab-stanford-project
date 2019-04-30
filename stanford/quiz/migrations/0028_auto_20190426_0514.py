# Generated by Django 2.1.5 on 2019-04-26 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0027_auto_20190425_0330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='job',
            field=models.CharField(choices=[('EMTA', 'EMT A'), ('EMTB', 'EMT B'), ('PARA', 'Paramedic'), ('PHYS', 'Physician'), ('NUR', 'Nurse'), ('STU', 'Student'), ('OTH', 'Other')], default='OTH', max_length=4),
        ),
    ]