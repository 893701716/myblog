# Generated by Django 2.0 on 2019-06-06 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0003_message_pubtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='pubtime',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]
