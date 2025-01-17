#!/usr/bin/env python

import sys

from django import setup
from django.conf import settings
from django.test.runner import DiscoverRunner


def runtests(*test_args):
    # Setup settings
    if not settings.configured:
        from django_generic_flatblocks.tests.testapp import settings as TEST_SETTINGS
        configure_args = dict((k,v) for k,v in TEST_SETTINGS.__dict__.items() if k.isupper())
        settings.configure(**configure_args)
    setup()
    test_runner = DiscoverRunner(verbosity=1)
    failures = test_runner.run_tests(['django_generic_flatblocks'])
    if failures:
        sys.exit(failures)


if __name__ == '__main__':
    runtests(*sys.argv[1:])
