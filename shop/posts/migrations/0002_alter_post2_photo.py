# Generated by Django 4.1.2 on 2022-11-11 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post2',
            name='photo',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
