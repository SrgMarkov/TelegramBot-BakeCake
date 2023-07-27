# Generated by Django 4.2.3 on 2023-07-27 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bake_cake_bot', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='email',
        ),
        migrations.RemoveField(
            model_name='users',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='users',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='users',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='users',
            name='name',
            field=models.CharField(max_length=256, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='users',
            name='phone',
            field=models.CharField(max_length=20, null=True, verbose_name='Phone Number'),
        ),
    ]
