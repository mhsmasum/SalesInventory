# Generated by Django 3.0.1 on 2020-01-02 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UnitofMeasure', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unitofmeasuredetails',
            name='uomid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='UnitofMeasure.UnitofMeasure'),
        ),
    ]
