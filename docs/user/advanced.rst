
.. _advanced:

Advanced settings
==================

Modifying default environments
-------------------------------

To modify the default environments you have to provide a dictionary to the SmartSettings constructor::

    import smartsettings
    smartsettings.config({
            'FLAVOURS': (
            'DEV',
            'STAGING',
            'PRODUCTION',
        ),
        'DEFAULT': 'DEV'  # default flavour always loads localsettings.py!
    }, globals())

This dictionary must contain 2 keys:

 * FLAVOURS – tuple or a list defining the environments
 * DEFAULT – name of the default DEV environment

Imported incremental settings file is determined by formula::
<lowercase flavour name>settings.py

Hence STAGING flavour will use file::
stagingsettings.py
