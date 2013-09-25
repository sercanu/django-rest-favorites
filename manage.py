#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    #os.environ.setdefault("DJANGO_SETTINGS_MODULE", "favorites.settings.local")
    if os.environ.get('HEROKU', '') == 'true' :
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "favorites.settings.heroku")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "favorites.settings.local")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
