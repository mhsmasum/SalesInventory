# Generated by Django 3.0.1 on 2020-01-07 05:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ItemColor', '0002_auto_20200107_1040'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemcolor',
            old_name='created_by',
            new_name='CreatedBy',
        ),
        migrations.RenameField(
            model_name='itemcolor',
            old_name='created_date',
            new_name='CreatedDate',
        ),
        migrations.RenameField(
            model_name='itemcolor',
            old_name='deleted_by',
            new_name='DeletedBy',
        ),
        migrations.RenameField(
            model_name='itemcolor',
            old_name='deleted_date',
            new_name='DeletedDate',
        ),
        migrations.RenameField(
            model_name='itemcolor',
            old_name='updated_by',
            new_name='UpdatedBy',
        ),
        migrations.RenameField(
            model_name='itemcolor',
            old_name='updated_date',
            new_name='UpdatedDate',
        ),
    ]