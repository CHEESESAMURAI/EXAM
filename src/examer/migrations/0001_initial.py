# Generated by Django 4.1 on 2022-08-04 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('name', models.CharField(max_length=255, verbose_name='Предмет')),
            ],
            options={
                'verbose_name': 'Экзамен',
                'verbose_name_plural': 'Список Экзаменов',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('name', models.CharField(max_length=255, verbose_name='Название потока')),
                ('visible', models.BooleanField(default=False, verbose_name='Скрыктый поток')),
            ],
            options={
                'verbose_name': 'Поток',
                'verbose_name_plural': 'Список потоков',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('date_time', models.DateTimeField()),
                ('link', models.CharField(max_length=4000)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='examer.exam', verbose_name='Экзамен')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='examer.group', verbose_name='Поток')),
            ],
            options={
                'verbose_name': 'Событие',
                'verbose_name_plural': 'Список событий',
            },
        ),
    ]