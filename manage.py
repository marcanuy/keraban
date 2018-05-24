#!/usr/bin/env python
import os
import sys

import dotenv


if __name__ == "__main__":
    env_file = '.env'
    if os.path.isfile(env_file):
        dotenv.read_dotenv(env_file)

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "keraban.settings.dev")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
