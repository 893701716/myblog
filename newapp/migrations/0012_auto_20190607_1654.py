# Generated by Django 2.0 on 2019-06-07 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0011_message_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='leavemessage',
            field=models.TextField(max_length=10000),
        ),
    ]
