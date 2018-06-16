# Generated by Django 2.0.1 on 2018-06-15 00:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=300)),
                ('is_correct', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('sponsor', models.CharField(max_length=50)),
                ('is_challenge', models.BooleanField()),
                ('image', models.ImageField(default='default.jpg', upload_to='category_images')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=300)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('max_time', models.DurationField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='quiz.Category')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionUserData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_started', models.DateTimeField(default=django.utils.timezone.now)),
                ('time_completed', models.DateTimeField(null=True)),
                ('answer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question_data', to='quiz.Answer')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_data', to='quiz.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Enter Name', max_length=100)),
                ('location', models.CharField(default='Enter location', max_length=100)),
                ('description', models.CharField(default='Enter description', max_length=500)),
                ('image', models.ImageField(blank=True, upload_to='profile_images')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='questionuserdata',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='question_data', to='quiz.Student'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='quiz.Question'),
        ),
        migrations.AlterUniqueTogether(
            name='questionuserdata',
            unique_together={('question', 'student')},
        ),
    ]