# -*- coding: utf-8 -*-

"""
Created on 2022-09-03
:author:  ()
"""

pytest_plugins = "kotti"

from pytest import fixture


@fixture(scope='session')
def custom_settings():
    import kotti_ai.resources
    kotti_ai.resources  # make pyflakes happy
    return {
        'kotti.configurators': 'kotti_tinymce.kotti_configure '
                               'kotti_ai.kotti_configure'}
