# Generated by Django 2.0 on 2019-06-09 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0016_auto_20190609_0841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='pubtime',
            field=models.DateTimeField(verbose_name='-date published'),
        ),
    ]
