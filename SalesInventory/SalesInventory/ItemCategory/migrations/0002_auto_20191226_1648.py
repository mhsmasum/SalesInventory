# Generated by Django 2.2.9 on 2019-12-26 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ItemCategory', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemcategory',
            old_name='create_by',
            new_name='created_by',
        ),
        migrations.RenameField(
            model_name='itemcategory',
            old_name='create_date',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='itemcategory',
            old_name='delete_by',
            new_name='deleted_by',
        ),
        migrations.RenameField(
            model_name='itemcategory',
            old_name='delete_date',
            new_name='deleted_date',
        ),
        migrations.RenameField(
            model_name='itemcategory',
            old_name='update_by',
            new_name='updated_by',
        ),
        migrations.RenameField(
            model_name='itemcategory',
            old_name='update_date',
            new_name='updated_date',
        ),
    ]