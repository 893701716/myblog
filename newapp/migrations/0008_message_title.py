# Generated by Django 2.0 on 2019-06-07 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0007_auto_20190606_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='title',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
