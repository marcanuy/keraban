# keraban
An inflexible, opinionated CMS based on Wagtail. 

Design a corporate website and give your client an user to
keep the content they desire up to date.

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [keraban](#keraban)
- [Goals](#goals)
    - [Design Principles](#design-principles)
- [Explanation](#explanation)
- [Features](#features)
- [Installation](#installation)
- [Running](#running)
    - [Admin](#admin)
- [How to](#how-to)
    - [Add a Page to main menu](#add-a-page-to-main-menu)
    - [Add a feature](#add-a-feature)
    - [Change Business info](#change-business-info)
        - [Change business data](#change-business-data)
        - [Add business social network](#add-business-social-network)
- [To do](#to-do)
- [Credits](#credits)
- [Ideas and Questions](#ideas-and-questions)

<!-- markdown-toc end -->

# Goals

Build and deploy websites that **can be easily maintained by non
developer users**.

## Design Principles

- Consistent look & feel through all web pages
- Implementation of web best practices:
  - *Semantic web*: Schema.org meta tags
  - Optimized for Search Engines (SEO, Google's richsnippets)
- Fully responsive
- Add and remove pages from backend

# Explanation

Most corporate websites shares the same content structure, their needs
typically consist of the following pages:

- homepage
- photo gallery
- features
- testimonials
- contact

This structure is most seen in websites for:

- Clinics
- Dentists
- Business
- Any organization that has a physical address and offer some kind of
  service.

# Features

- Based on Wagtail (Django CMS)
  - Amazing back-end
- Fully Responsive (Bootstrap 4 grid system)
- Icons (FontAwesome <https://fontawesome.com/v4.7.0/icons/>)
- SEO
  - Using Schema.org
  - Social Markup <https://developers.google.com/webmasters/social-markup>
  - Knowledge Graph card with details about the business <https://developers.google.com/search/docs/data-types/local-business>
- SASS with Bootstrap variables available
- Contact form with <https://formspree.io/> (doesn't need email server
  configuration)

# Notes

- static files: **whitenoise**
	- locally with `runserver` and
	- in production
- environment variables: **django-dotenv**
- media: TODO implement django-storages

# Installation

Create a virtual environment:

    mkvirtualenv --python=/usr/bin/python3.6 ~/.virtualenvs/keraban
Or

	python3.6 -m venv ~/.virtualenvs/keraban/
	
Clone the repo:

	git clone git@github.com:marcanuy/keraban.git

Use new site:

	cd keraban
    echo `pwd` > ~/.virtualenvs/keraban/.project
	workon keraban	

# Running locally

./manage.py runserver

## Admin

<http://localhost:8000/admin/login/?next=/admin/>

Super admin credentials:

- user: admin
- pass: mypass1234

# Deploy

Adjust after deployment:

- Use `settings/production.py`
- Set environment variables:
  - ALLOWED_HOSTS (DJANGO_ALLOWED_HOSTS)
  - customize `/_env.skeleton` and copy it to `/.env` 
	- <https://github.com/jpadilla/django-dotenv>
# How to

## Add a Page to main menu

In **Admin** go to **Page / Edit / Promote** and select **Show in menus**.

## Add a feature

In **Admin** go to **Page / Home**, locate the **Features index page**
and **Add Child Page**.

## Change Business info

### Change business data

In **Admin** go to **Business Misc / Businesses** and **Edit**
Business info.

### Add business social network

In **Admin** go to **Business Misc / Social Networks** and locate the
button **Add Social Profiles**.


# To do

- change featurettes to a flexible streamfield of alternating pages
- add boostrap form classes to contact form template
- make carousel on homepage hero items
- add google maps api key
- add business opening hours snippet
- load bootstrap from nodejs or django/wagtail package
- add schema
  - <https://developers.google.com/search/docs/data-types/local-business>
  - <https://developers.google.com/search/docs/data-types/breadcrumb>
  - <https://developers.google.com/webmasters/social-markup/#adding_structured_markup_to_your_site>
- business data and social profiles as settings? <http://docs.wagtail.io/en/v2.0/reference/contrib/settings.html>
- add sharing on social buttons <https://github.com/fcurella/django-social-share#templates>
- footer with icons and list (similar to
  <https://stackoverflow.com/q/48519250/1165509> and <https://getbootstrap.com/docs/4.0/examples/pricing/>)
- Possibility to use any numbers of featurettes pages in homepage (ListBlock)
  implementing it as a StreamBlock
- add favicon
- extend support for more specific Organization types <http://schema.org/Organization>
- better integration of location page and business data address/location

# Credits

- Powered by <wagtail.io>
- Inspired by the amazing Wagtail Bakery Demo
  <https://github.com/wagtail/bakerydemo/>
- Galleries layout based on <https://tutorialzine.com/2018/03/3-amazing-bootstrap-4-gallery-templates>
  
# Ideas and Questions

- <https://twitter.com/marcanuy/>
- <https://github.com/marcanuy/keraban/issues>
