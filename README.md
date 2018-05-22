# keraban
An inflexible, opinionated CMS based on Wagtail. 

Design a corporate website and give your client an user to
keep the content they desire up to date.

See it live! http://keraban.marcanuy.com/

The Keraban website is an example of what a typical site looks like,
the site itself its made with it.

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [keraban](#keraban)
- [Goals](#goals)
    - [Design Principles](#design-principles)
- [Explanation](#explanation)
- [Features](#features)
- [Notes](#notes)
- [Installation](#installation)
- [Running locally](#running-locally)
    - [Admin](#admin)
- [Deploy](#deploy)
- [How to](#how-to)
    - [Add a Page to main menu](#add-a-page-to-main-menu)
    - [Add a feature](#add-a-feature)
    - [Change Business info](#change-business-info)
        - [Change business data](#change-business-data)
        - [Add business social network](#add-business-social-network)
- [Models](#models)
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
- Add / Remove / Edit pages from Backend by end users

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
- Google Maps in Location page
  - <https://developers.google.com/maps/documentation/embed/guide>
  
# Notes

- static files: **whitenoise**
	- locally with `runserver` and
	- in production
- environment variables: **django-dotenv**
- media: **django-storages**
- google analytics: **django-analytical**

# Installation

1. Create a virtual environment:

        mkvirtualenv --python=/usr/bin/python3.6 ~/.virtualenvs/keraban

  Or

	    python3.6 -m venv ~/.virtualenvs/keraban/
	
2. Clone the repo:

    	git clone git@github.com:marcanuy/keraban.git

3. Use new site:

    	cd keraban
        echo `pwd` > ~/.virtualenvs/keraban/.project
    	workon keraban	

4. Generate site CSS

    	make compile-sass
	
5. Load fixture

        ./manage.py loaddata home/fixtures/keraban.json


# Running locally

    ./manage.py runserver

## Admin

<http://localhost:8000/admin/login/?next=/admin/>

Super admin credentials:

- user: admin
- pass: mypass1234

# Deploy

Adjust server after getting the files on the server:

1. Copy `/_env.skeleton` to `/.env`
2. Customize `/.env` with your environment variables values
   - `.env` is processed by <https://github.com/jpadilla/django-dotenv>
   - Choose to use `keraban.settings.production` as the `DJANGO_SETTINGS_MODULE`
   - Adjust ALLOWED_HOSTS by setting `DJANGO_ALLOWED_HOSTS`
   - Set up Amazon S3: 
	 - Create an user with programmatic access
		 - Create group for that user with **AmazonS3FullAccess** as the
		 attached policy
		 - 	generate a key with IAM
               <https://console.aws.amazon.com/iam/home>)
	 - Then you can fill the following keys for handling media
		 - AWS_ACCESS_KEY_ID
		 - AWS_SECRET_ACCESS_KEY
		 - AWS_REGION
		 - AWS_STORAGE_BUCKET_NAME (will be created if not exists)
   - Get Google maps api key
     <https://developers.google.com/maps/documentation/embed/get-api-key>
	 to fill GOOGLE_MAP_API_KEY and restrict its usage accepting
     requests from your website at <https://console.developers.google.com/apis/credentials>

# How to

## Add a Page to main menu

In **Admin** go to **Page / Edit / Promote** and select **Show in menus**.

## Add a feature

In **Admin** go to **Page / Home**, locate the **Features index page**
and **Add Child Page**.

## Change Business info

### Change business data

In **Admin** go to **Business Misc / Organization** and **Edit**
Business info.

### Add business social network

In **Admin** go to **Business Misc / Social Networks** and locate the
button **Add Social Profiles**.

# Models

![models](docs/keraban_models.png?raw=true)

# To do

- change featurettes to a flexible streamfield of alternating pages
- add boostrap form classes to contact form template
- make carousel on homepage hero items
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

- Powered by https://wagtail.io
- Inspired by the amazing Wagtail Bakery Demo
  <https://github.com/wagtail/bakerydemo/>
- Galleries layout based on <https://tutorialzine.com/2018/03/3-amazing-bootstrap-4-gallery-templates>
  
# Ideas and Questions

- <https://twitter.com/marcanuy/>
- <https://github.com/marcanuy/keraban/issues>
