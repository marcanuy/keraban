# Generated by Django 2.0.5 on 2018-05-18 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactpage',
            name='thanks_page',
            field=models.ForeignKey(blank=True, help_text='Choose the page with the thanks message that will be shown after the form is sent', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page', verbose_name='Thanks Page'),
        ),
    ]