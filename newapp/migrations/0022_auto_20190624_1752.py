# Generated by Django 2.0 on 2019-06-24 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0021_auto_20190619_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='image',
            field=models.ImageField(max_length=5, upload_to='newapp/static/newapp/userupload/'),
        ),
    ]