# Generated by Django 3.0.1 on 2020-01-05 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ItemCategory', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemcategory',
            old_name='created_by',
            new_name='CreatedBy',
        ),
        migrations.RenameField(
            model_name='itemcategory',
            old_name='created_date',
            new_name='CreatedDate',
        ),
        migrations.RenameField(
            model_name='itemcategory',
            old_name='deleted_by',
            new_name='DeletedBy',
        ),
        migrations.RenameField(
            model_name='itemcategory',
            old_name='deleted_date',
            new_name='DeletedDate',
        ),
        migrations.RenameField(
            model_name='itemcategory',
            old_name='updated_by',
            new_name='UpdatedBy',
        ),
        migrations.RenameField(
            model_name='itemcategory',
            old_name='updated_date',
            new_name='UpdatedDate',
        ),
    ]
