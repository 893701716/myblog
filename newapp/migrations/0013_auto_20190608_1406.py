# Generated by Django 2.0 on 2019-06-08 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0012_auto_20190607_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='pubtime',
            field=models.DateTimeField(verbose_name='-date published'),
        ),
        migrations.AlterField(
            model_name='message',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newapp.Visitor'),
        ),
    ]
