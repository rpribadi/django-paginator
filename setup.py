from setuptools import setup, find_packages

version = '1.0.0'

LONG_DESCRIPTION = """
How to use django-paginator
----------------------------

1. List this application in the ``INSTALLED_APPS`` portion of your settings
   file.  Your settings file might look something like::
   
       INSTALLED_APPS = (
           # ...
           'paginator',
       )

2. If it's not already added in your setup, add the request context processor.
   Note that context processors are set by default implicitly, so to set them
   explicitly, you need to copy and paste this code into your under
   the value TEMPLATE_CONTEXT_PROCESSORS::
   
        ("django.core.context_processors.auth",
        "django.core.context_processors.debug",
        "django.core.context_processors.i18n",
        "django.core.context_processors.media",
        "django.core.context_processors.request")

3. Add this line at the top of your template to load the pagination tags:

       {% load paginator_tags %}


4. Now you want to display the page navigation from paginator instance by using 
   the paginator filter:
   
       {{ paginator|render_nav }}
   
   This does not take any arguments, but does assume that you have already
   called autopaginate, so make sure to do so first.


That's it!  You have now paginated ``object_list`` and given users of the site
a way to navigate between the different pages--all without touching your views.


Optional Settings
------------------
In django-paginator, there are no required settings.  There are, however, a
small set of optional settings useful for changing the default behavior of the
pagination tags, such as:

``PAGINATOR_PER_PAGE``
    Default value: 10
    The default amount of items to show on a page if no number is specified.

``PAGINATOR_MAX_PAGE_NAV``
    Default value: 5
    The number of main page items.

``PAGINATOR_MAX_JUMPER``
    Default value: 2
    The number of jumper page items on left / right side

``PAGINATOR_RAISE_404_ON_INVALID_PAGE``
    Default value: False
    Determines whether an invalid page raises an ``Http404`` or just sets the
    ``invalid_page`` context variable.  ``True`` does the former and ``False``
    does the latter.
"""

setup(
    name='django-paginator',
    version=version,
    description="django-paginator",
    long_description=LONG_DESCRIPTION,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
    keywords='pagination,django',
    author='Riki Pribadi',
    author_email='pribadi.riki@gmail.com',
    url='https://github.com/rpribadi/django-paginator',
    license='',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
