# Generated by Django 2.2.16 on 2022-08-05 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20220804_1333'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('slug', models.SlugField(unique=True, verbose_name='Идентификатор')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
        ),
    ]
