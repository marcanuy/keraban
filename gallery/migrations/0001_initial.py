# Generated by Django 2.0.5 on 2018-05-18 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0005_auto_20180517_1319'),
        ('wagtailcore', '0040_page_draft_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryIndexPage',
            fields=[
                ('standardpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.StandardPage')),
            ],
            options={
                'abstract': False,
            },
            bases=('home.standardpage',),
        ),
        migrations.CreateModel(
            name='GalleryPage',
            fields=[
                ('standardpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.StandardPage')),
                ('collection', models.ForeignKey(blank=True, help_text='Select the image collection for this gallery.', limit_choices_to=models.Q(_negated=True, name__in=['Root']), null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailcore.Collection')),
            ],
            options={
                'abstract': False,
            },
            bases=('home.standardpage',),
        ),
    ]