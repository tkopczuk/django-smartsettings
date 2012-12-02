# -*- coding: utf-8 -*-
from distutils.core import setup
setup(
    name="django-smartsettings",
    packages=["smartsettings"],
    version="0.1.0",
    description="Django settings manager for easy development and easy deployment with no place for mistakes.",
    author="Tomek Kopczuk",
    author_email="tomek@bladepolska.com",
    url="http://www.django-smartsettings.com/",
    download_url="https://github.com/tkopczuk/django-smartsettings/archive/v0.1.0.tar.gz",
    keywords=["django", "settings", "manager", "settings manager"],
    classifiers=[
            "Development Status :: 4 - Beta",
            "Environment :: Console",
            "Framework :: Django",
            "Intended Audience :: Developers",
            "Intended Audience :: System Administrators",
            "License :: OSI Approved :: ISC License",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 2.7",
            "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries",
            "Topic :: Software Development :: Libraries :: Python Modules",
            "Topic :: Software Development :: Build Tools",
        ],
    long_description="""\
Multi-environment settings for multi-dev projects.

-------------------------------------
Developers should never have to worry before running anything on their machines.
It should never run on production database by accident.

On the other hand production often need a different set of middlewares or configs.
These need to be tested as well. By developers.

Never run on Production by accident and never run Production on your local settings ever again.
But do anything you want if you want to. Easily.

-------------------------------------

By default we define 2 environments: production and dev.

You can define as many environments as you want.
E.g. staging is the usual choice.

-------------------------------------

Switching environments is as easy as executing:
export ENV_FLAVOUR=PRODUCTION

When you close your terminal window, your shell session will start from the scratch
and you will be running on DEV again.

No mistakes!

-------------------------------------

This version has been tested and is completely compatible with the latest
Django trunk (1.5).

It is probably compatible with Django >=1.0.

-------------------------------------

This library solves the problem of managing multiple settings for development,
staging, production and any other type of environment you can think of.

Designed for DVCS development, handles local settings for each developer.

Django-Environments supports the right configuration pattern:
  – type of environment defined in ENV
  – never run on Production by accident – we default to Development
  – local settings are easily .gitignore'd
"""
)
