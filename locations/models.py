from django.conf import settings

from home.models import StandardPage

class LocationPage(StandardPage):
    """
    Detail for the specific business location.
    """
    def __str__(self):
        return self.title

    # Makes additional context available to the template so that we can access
    # the latitude, longitude and map API key to render the map
    def get_context(self, request):
        context = super(LocationPage, self).get_context(request)
        context['google_map_api_key'] = settings.GOOGLE_MAP_API_KEY
        return context
