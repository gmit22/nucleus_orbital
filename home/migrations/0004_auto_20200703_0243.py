# Generated by Django 3.0.7 on 2020-07-02 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200703_0235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sport',
            name='start',
        ),
        migrations.RemoveField(
            model_name='sport',
            name='stop',
        ),
        migrations.AddField(
            model_name='sport',
            name='Timing',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
    ]
