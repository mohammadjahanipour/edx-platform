"""  # lint-amnesty, pylint: disable=django-not-configured
Import celery, load its settings from the django settings
and auto discover tasks in all installed django apps.

Taken from: https://celery.readthedocs.org/en/latest/django/first-steps-with-django.html
"""


import os


# Set the default Django settings module for the 'celery' program
# and then instantiate the Celery singleton.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cms.envs.production')
