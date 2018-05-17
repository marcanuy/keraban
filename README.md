# keraban
An inflexible, opinionated CMS based on Wagtail. 

Design a corporate website and give your client an user to
keep the content they desire up to date.

# Goal

Build and deploy websites easily that **can be maintained by non
developer users**.

# Explanation

Most corporate websites shares the same content structure, they
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

# Installation

Create a virtual environment:

    mkvirtualenv --python=/usr/bin/python3.6 ~/.virtualenvs/keraban
	
Clone the repo:

	git clone git@github.com:marcanuy/keraban.git

Use new site:

	cd keraban
    echo `pwd` > ~/.virtualenvs/keraban/.project
	workon keraban	

# Running

./manage.py runserver

## Admin

<http://localhost:8000/admin/login/?next=/admin/>

Super admin credentials:

- user: admin
- pass: mypass1234

# To do

- make carousel on homepage hero items
- load bootstrap from nodejs
- add schema
  - <https://developers.google.com/search/docs/data-types/local-business>
  - <https://developers.google.com/search/docs/data-types/breadcrumb>
  - <https://developers.google.com/webmasters/social-markup/#adding_structured_markup_to_your_site>
- business data as settings? <http://docs.wagtail.io/en/v2.0/reference/contrib/settings.html>
- add sharing on social buttons <https://github.com/fcurella/django-social-share#templates>
- footer with icons and list (similar to
  <https://stackoverflow.com/q/48519250/1165509> and <https://getbootstrap.com/docs/4.0/examples/pricing/>)
- Possibility to use any numbers of featurettes pages in homepage (ListBlock)
  implementing it as a StreamBlock
- add favicon
