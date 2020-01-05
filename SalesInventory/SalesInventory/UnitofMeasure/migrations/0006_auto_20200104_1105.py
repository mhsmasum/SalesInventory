# Generated by Django 3.0.1 on 2020-01-04 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UnitofMeasure', '0005_unitofmeasure_isdeleted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unitofmeasure',
            name='isdeleted',
        ),
        migrations.AddField(
            model_name='unitofmeasure',
            name='created_by',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='unitofmeasure',
            name='created_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='unitofmeasure',
            name='deleted_by',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='unitofmeasure',
            name='deleted_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='unitofmeasure',
            name='updated_by',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='unitofmeasure',
            name='updated_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]