# Generated by Django 4.0.2 on 2022-02-20 23:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admob_name', models.CharField(max_length=255, unique=True, verbose_name='Название AdMob')),
                ('admob_secret_file', models.JSONField(max_length=255, unique=True, verbose_name='Секретный файл AdMob')),
                ('publisher_id', models.CharField(max_length=100, null=True, unique=True, verbose_name='Секретный файл AdMob')),
            ],
        ),
        migrations.CreateModel(
            name='Apps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_id', models.CharField(max_length=255, unique=True, verbose_name='ID приложения')),
                ('add_time', models.DateTimeField(verbose_name='Время добавления')),
                ('app_name', models.CharField(default='Не существует', max_length=255, verbose_name='Название приложения')),
                ('last_update', models.CharField(default='Не существует', max_length=255, verbose_name='Последнее обновление')),
                ('installs', models.IntegerField(default=0, verbose_name='Всего установок')),
                ('status', models.BooleanField(default=False, verbose_name='Статус')),
                ('admob', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.admobs')),
            ],
        ),
        migrations.CreateModel(
            name='Developers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dev', models.CharField(max_length=255, verbose_name='Разработчик')),
            ],
        ),
        migrations.CreateModel(
            name='Folders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folder_name', models.CharField(max_length=255, unique=True, verbose_name='Название папки')),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(verbose_name='Дата/время')),
                ('installs', models.IntegerField(verbose_name='Установки')),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.apps')),
            ],
        ),
        migrations.AddField(
            model_name='apps',
            name='folder',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='crm.folders'),
        ),
    ]