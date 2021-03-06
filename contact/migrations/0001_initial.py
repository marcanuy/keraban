# Generated by Django 2.0.5 on 2018-05-17 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('home', '0005_auto_20180517_1319'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactPage',
            fields=[
                ('standardpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.StandardPage')),
                ('email', models.CharField(help_text='The email address that receives submitted forms.', max_length=100, verbose_name='Business email address')),
                ('thanks_page', models.ForeignKey(blank=True, help_text='Choose the page with the thanks message that will be shown after the form is sent', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page', verbose_name='Hero CTA link')),
            ],
            options={
                'abstract': False,
            },
            bases=('home.standardpage',),
        ),
    ]
