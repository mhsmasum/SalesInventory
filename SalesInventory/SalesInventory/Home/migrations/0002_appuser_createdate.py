# Generated by Django 3.0.1 on 2019-12-24 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='CreateDate',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]