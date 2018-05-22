
"""
Supported phone numbers types supported by Google:

-customer service
-technical support
-billing support
-bill payment
-sales
-reservations
-credit card support
-emergency
-baggage tracking
-roadside assistance
-package tracking

Source: https://developers.google.com/search/docs/data-types/corporate-contact
"""
CONTACT_TYPES_CHOICES = (
    ('CS', 'customer service'),
    ('TS', 'technical support'),
    ('BS', 'billing support'),
    ('BP', 'bill payment'),
    ('S', 'sales'),
    ('R', 'reservations'),
    ('CC', 'credit card support'),
    ('E', 'emergency'),
    ('BT', 'baggage tracking'),
    ('RA', 'roadside assistance'),
    ('PT', 'package tracking'),
)
