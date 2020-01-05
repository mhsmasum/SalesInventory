# Generated by Django 3.0.1 on 2020-01-05 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemcolor_name', models.CharField(max_length=200)),
                ('itemcolor_name_bangla', models.CharField(blank=True, max_length=200, null=True)),
                ('itemcolor_remarks', models.CharField(blank=True, max_length=200, null=True)),
                ('itemcolor_code', models.CharField(blank=True, max_length=200, null=True)),
                ('isactive', models.BooleanField(default=True)),
                ('created_by', models.CharField(blank=True, max_length=200, null=True)),
                ('created_date', models.DateTimeField(blank=True, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=200, null=True)),
                ('updated_date', models.DateTimeField(blank=True, null=True)),
                ('deleted_by', models.CharField(blank=True, max_length=200, null=True)),
                ('deleted_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]