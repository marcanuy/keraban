from wagtail.contrib.modeladmin.options import (
    ModelAdmin, ModelAdminGroup, modeladmin_register)

from .models import Organization, SocialProfiles, ContactNumbers

class ContactNumbers(ModelAdmin):
    model = ContactNumbers
    menu_icon = 'fa-phone'
    menu_order = 300
    
class SocialProfilesModelAdmin(ModelAdmin):
    model = SocialProfiles
    #menu_label = 'Social Profiles'
    menu_icon = 'fa-smile-o'
    list_display = ('name', 'url', 'icon')
    menu_order = 200

class OrganizationModelAdmin(ModelAdmin):
    model = Organization
    menu_order = 000
    
class BusinessModelAdminGroup(ModelAdminGroup):
    menu_label = 'Business Misc'
    menu_icon = 'fa-building-o'
    menu_order = 300  # will put in 4th place (000 being 1st, 100 2nd)
    items = (OrganizationModelAdmin,SocialProfilesModelAdmin, ContactNumbers)
    
modeladmin_register(BusinessModelAdminGroup)
