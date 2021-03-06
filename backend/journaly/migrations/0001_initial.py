# Generated by Django 4.0.2 on 2022-03-07 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('location', models.CharField(max_length=200)),
                ('bio', models.CharField(max_length=250)),
                ('avatar', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('journal_title', models.CharField(max_length=200)),
                ('mood_rating', models.IntegerField()),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journaly.calendar')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journaly.user')),
            ],
        ),
        migrations.CreateModel(
            name='Exercises',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise_name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('image_url', models.ImageField(upload_to='')),
                ('source_url', models.URLField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journaly.user')),
            ],
        ),
    ]
