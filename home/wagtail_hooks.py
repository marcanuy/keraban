from wagtail.contrib.modeladmin.options import (
    ModelAdmin, ModelAdminGroup, modeladmin_register)

from .models import Businesses, SocialProfiles#, FooterText

class SocialProfilesModelAdmin(ModelAdmin):
    model = SocialProfiles
    #menu_label = 'Social Profiles'
    menu_icon = 'fa-smile-o'
    list_display = ('name', 'url', 'icon')

class BusinessesModelAdmin(ModelAdmin):
    model = Businesses

class BusinessModelAdminGroup(ModelAdminGroup):
    menu_label = 'Business Misc'
    menu_icon = 'fa-building-o'
    menu_order = 300  # will put in 4th place (000 being 1st, 100 2nd)
    items = (SocialProfilesModelAdmin, BusinessesModelAdmin)
    
modeladmin_register(BusinessModelAdminGroup)
