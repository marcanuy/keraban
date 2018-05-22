from home.models import StandardPage, Organization

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
        business = Organization.objects.first()
        context['address'] = business.address
        return context
