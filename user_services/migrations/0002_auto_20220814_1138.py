# Generated by Django 3.0 on 2022-08-14 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=30, unique=True, verbose_name='user name'),
        ),
    ]