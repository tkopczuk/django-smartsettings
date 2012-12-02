# Created by Tomek Kopczuk, @tkopczuk
# Copyright (c) 2012, Blade Polska s.c., contact@bladepolska.com

# Permission to use, copy, modify, and/or distribute this software for any purpose with or
# without fee is hereby granted, provided that the above copyright notice and this permission
# notice appear in all copies.

# THE SOFTWARE IS PROVIDED “AS IS” AND THE AUTHOR DISCLAIMS ALL
# WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE
# AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR
# CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING
# FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF
# CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

__title__ = 'smartsettings'
__version__ = '0.1.0'
__author__ = 'Tomek Kopczuk'
__license__ = 'ISC'
__copyright__ = 'Copyright 2012 Tomek Kopczuk'

from django.utils import importlib
import os
import sys

from . import messages


def exit_with_error(error="", error_format_args=[], info=None, info_format_args=[]):
    if info:
        print ""
        print "!!! INFO !!!"
        print info % info_format_args

    print ""
    print "!!! ERROR - ACTION REQUIRED !!!"
    print ""
    print error % error_format_args
    print ""

    sys.exit(-1)


def get_running_flavour():
    return os.environ.get('ENV_FLAVOUR', 'DEV')


def validate_and_heal_db_settings(foreign_globals):
    def validate_db_settings():
        return 'DATABASES' in foreign_globals and 'default' in foreign_globals['DATABASES'] and foreign_globals['DATABASES']['default'] != {}

    if not validate_db_settings():
        import dj_database_url

        default_db = foreign_globals.get('DATABASE_URL', None)
        if default_db:
            foreign_globals['DATABASES'] = {'default': dj_database_url.config(default=default_db)}
        else:
            foreign_globals['DATABASES'] = {'default': dj_database_url.config()}

    if not validate_db_settings():
        exit_with_error(error=messages.NO_DB)


def get_module_directory(module_string):
    module = importlib.import_module(module_string)
    return os.path.dirname(module.__file__)


def load_settings_from_module(module_string):
    module = importlib.import_module(module_string)
    return module.__dict__


def update_globals_with_settings(foreign_globals, settings):
    for k, v in settings.items():
        if k.startswith('__') and k.endswith('__'):
            continue
        foreign_globals[k] = v


DEFAULT_SETTINGS = {
    'FLAVOURS': ('DEV', 'PRODUCTION'),
    'DEFAULT': 'DEV'  # default flavour always loads localsettings.py!
}


def config(foreign_globals, settings=DEFAULT_SETTINGS):
    assert 'FLAVOURS' in settings, \
                "You have to provide 'django-environment-flavours' \
                with 'FLAVOURS' setting."
    assert isinstance(settings['FLAVOURS'], tuple) or isinstance(settings['FLAVOURS'], list), \
                "'django-environment-flavours 'FLAVOURS' setting \
                must be a dict."

    FLAVOURS = settings['FLAVOURS']
    assert len(FLAVOURS) > 0, \
                "'django-environment-flavours 'FLAVOURS' setting \
                must contain at least 1 flavour."

    DEFAULT_FLAVOUR = settings.get('DEFAULT', 'DEV')
    assert DEFAULT_FLAVOUR in FLAVOURS, \
                "'django-environment-flavours 'FLAVOURS' setting \
                must contain the DEFAULT '%s' flavour." % DEFAULT_FLAVOUR

    RUNNING_FLAVOUR = get_running_flavour()

    if not RUNNING_FLAVOUR in FLAVOURS:
        exit_with_error(info=messages.HOW_TO_SWITCH_FLAVOUR_INFO,
                        error=messages.WRONG_FLAVOUR_ERROR,
                        error_format_args=RUNNING_FLAVOUR)

    SETTINGS_IMPORT_MODULE_COMPONENTS = foreign_globals['__name__'].split('.')
    if len(SETTINGS_IMPORT_MODULE_COMPONENTS) > 1:
        BASE_MODULE_PATH = '.'.join(SETTINGS_IMPORT_MODULE_COMPONENTS[:-1])
    else:
        BASE_MODULE_PATH = ''

    FLAVOUR_MODULE = "%s.%ssettings" % (BASE_MODULE_PATH, RUNNING_FLAVOUR.lower())
    try:
        settings = load_settings_from_module(FLAVOUR_MODULE)
    except Exception as e:
        exit_with_error(error=messages.CANNOT_LOAD_FLAVOUR_ERROR,
                        error_format_args={
                            'module': FLAVOUR_MODULE,
                            'exception': e
                        })

    update_globals_with_settings(foreign_globals, settings)

    if (RUNNING_FLAVOUR == DEFAULT_FLAVOUR):
        settings_modules_path = '.'.join(FLAVOUR_MODULE.split('.')[:-1])
        local_settings_module = "%s.localsettings" % settings_modules_path
        try:
            local_settings = load_settings_from_module(local_settings_module)
        except Exception as e:
            exit_with_error(error=messages.NO_LOCAL_SETTINGS_FILE,
                            error_format_args={
                                'settings_path': get_module_directory(FLAVOUR_MODULE),
                                'exception': e
                            })

        update_globals_with_settings(foreign_globals, local_settings)

    validate_and_heal_db_settings(foreign_globals)

    print "Running env. flavour:", RUNNING_FLAVOUR
