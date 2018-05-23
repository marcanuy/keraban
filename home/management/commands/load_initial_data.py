import os

from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.management import call_command

from wagtail.core.models import Site, Page


class Command(BaseCommand):
    """
    Original: https://github.com/wagtail/bakerydemo/blob/master/bakerydemo/base/management/commands/load_initial_data.py
    """
    def handle(self, **options):
        fixtures_dir = os.path.join(settings.BASE_DIR, 'home', 'fixtures')
        fixture_file = os.path.join(fixtures_dir, 'keraban.xml')

        # Wagtail creates default Site and Page instances during install, but we already have
        # them in the data load. Remove the auto-generated ones.
        if Site.objects.filter(hostname='localhost').exists():
            Site.objects.get(hostname='localhost').delete()
        if Page.objects.filter(title='Welcome to your new Wagtail site!').exists():
            Page.objects.get(title='Welcome to your new Wagtail site!').delete()

        call_command('loaddata', fixture_file, verbosity=0)

        print("Data loaded successfully...")
