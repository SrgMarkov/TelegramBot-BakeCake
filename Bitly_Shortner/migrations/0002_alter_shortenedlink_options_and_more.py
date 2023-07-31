# Generated by Django 4.2.3 on 2023-07-31 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bitly_Shortner', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shortenedlink',
            options={'verbose_name': 'Сокращенная ссылка', 'verbose_name_plural': 'Сокращенные ссылки'},
        ),
        migrations.RemoveField(
            model_name='shortenedlink',
            name='click_count',
        ),
        migrations.AddField(
            model_name='shortenedlink',
            name='link_title',
            field=models.CharField(blank=True, max_length=200, verbose_name='Название ссылки'),
        ),
        migrations.AlterField(
            model_name='shortenedlink',
            name='original_link',
            field=models.URLField(verbose_name='Оригинальная ссылка'),
        ),
        migrations.AlterField(
            model_name='shortenedlink',
            name='shortened_link',
            field=models.URLField(blank=True, verbose_name='Сокращенная ссылка'),
        ),
    ]
