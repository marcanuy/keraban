# Generated by Django 2.0.5 on 2018-05-22 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('home', '0007_homepage_featured_location'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Businesses',
            new_name='Organization',
        ),
        migrations.AlterModelOptions(
            name='organization',
            options={'verbose_name_plural': 'Organization'},
        ),
    ]
