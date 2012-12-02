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

# Infos
HOW_TO_SWITCH_FLAVOUR_INFO = \
"""You can switch flavours through env. variable ENV_FLAVOUR, e.g.:
'unset ENV_FLAVOUR' / 'export ENV_FLAVOUR=DEV' or
'export ENV_FLAVOUR=STAGING' or
'export ENV_FLAVOUR=PRODUCTION'."""

RUNNING_DEV_FLAVOUR_INFO = \
"""You are running a 'DEV' flavour.
This is a DEV-only error.

You can set another flavour through env, variable ENV_FLAVOUR, like:
'export ENV_FLAVOUR=<FLAVOUR>'."""

# Errors
WRONG_FLAVOUR_ERROR = \
"Wrong env. flavour setting: 'ENV_FLAVOUR=%s'."

CANNOT_LOAD_FLAVOUR_ERROR = \
"""Cannot load settings from module %(module)s due to exception:
%(exception)s"""

NO_LOCAL_SETTINGS_FILE = \
"""Cannot load your local dev. settings from file:
    '%(settings_path)s/localsettings.py'
due to exception:
    %(exception)s.

Ensure this file exists and can be imported:
    touch "%(settings_path)s/localsettings.py\""""

NO_DB = \
"""You need to set:
   1) DATABASE_URL env. variable
or 2) DATABASE_URL setting in localsettings.py.

E.g.:
DATABASE_URL='postgres://bb:bb@localhost/bb'"""
