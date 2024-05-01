# Generated by Django 4.1.2 on 2024-04-30 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ForParents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Тема информации')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Информация для родителей')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото для родителей')),
                ('link', models.CharField(blank=True, max_length=100, null=True, verbose_name='Ссыдка на источник')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='ForStudents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Тема информации')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Информация для учеников')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото для учеников')),
                ('link', models.CharField(blank=True, max_length=100, null=True, verbose_name='Ссыдка на источник')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='HelpfulInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Описание источника')),
                ('link', models.CharField(blank=True, max_length=100, null=True, verbose_name='Ссыдка на источник')),
            ],
        ),
        migrations.CreateModel(
            name='Methodically',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Тема информации')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Описание разработки')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото')),
                ('link', models.CharField(blank=True, max_length=100, null=True, verbose_name='Ссыдка на источник')),
            ],
        ),
        migrations.CreateModel(
            name='TeacherCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Ф.И.О.')),
                ('resume', models.TextField(blank=True, null=True, verbose_name='Краткое резюме учителя для главной страницы')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото на главную страницу')),
            ],
        ),
    ]
