# Generated by Django 4.1.2 on 2024-04-30 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='forparents',
            options={'ordering': ['-pub_date']},
        ),
        migrations.AlterModelOptions(
            name='forstudents',
            options={'ordering': ['-pub_date']},
        ),
    ]