# -*- coding: utf-8 -*-

"""
Created on 2022-09-03
:author:  ()
"""

from kotti.resources import File
from pyramid.i18n import TranslationStringFactory

_ = TranslationStringFactory('kotti_ai')


def kotti_configure(settings):
    """ Add a line like this to you .ini file::

            kotti.configurators =
                kotti_ai.kotti_configure

        to enable the ``kotti_ai`` add-on.

    :param settings: Kotti configuration dictionary.
    :type settings: dict
    """

    settings['pyramid.includes'] += ' kotti_ai'
    settings['kotti.alembic_dirs'] += ' kotti_ai:alembic'
    settings['kotti.available_types'] += ' kotti_ai.resources.CustomContent'
    settings['kotti.available_types'] += (
          ' kotti_ai.resources.Poll' +
          ' kotti_ai.resources.Choice' +
          ' kotti_ai.resources.AImage')
    settings['kotti.fanstatic.view_needed'] += ' kotti_ai.fanstatic.css_and_js'
    File.type_info.addable_to.append('CustomContent')
    File.type_info.addable_to.append('Poll')
    File.type_info.addable_to.append('AImage')
    # default_actions.append(LinkRenderer("my-custom-submenu"))
    
#     # 尝试增加菜单.这段要去掉 。若不行，则重新setup一下。
#     from kotti.util import Link
#     from kotti.views.site_setup import CONTROL_PANEL_LINKS

#     # def kotti_configure(settings):
#     link = Link('name', _(u'Title'))
#     CONTROL_PANEL_LINKS.append(link)
    
    from kotti.util import LinkRenderer
    from kotti.resources import default_actions

# def kotti_configure(settings):
    default_actions.append(LinkRenderer("my-custom-submenu"))


def includeme(config):
    """ Don't add this to your ``pyramid_includes``, but add the
    ``kotti_configure`` above to your ``kotti.configurators`` instead.

    :param config: Pyramid configurator object.
    :type config: :class:`pyramid.config.Configurator`
    """

    config.add_translation_dirs('kotti_ai:locale')
    config.add_static_view('static-kotti_ai', 'kotti_ai:static')

    config.scan(__name__)
