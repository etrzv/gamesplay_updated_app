# Generated by Django 4.1.2 on 2022-11-11 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
