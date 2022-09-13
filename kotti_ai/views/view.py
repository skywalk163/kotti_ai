# -*- coding: utf-8 -*-

"""
Created on 2022-09-03
:author:  ()
"""

from pyramid.view import view_config
from pyramid.view import view_defaults

from kotti_ai import _
from kotti_ai.resources import CustomContent
from kotti_ai.fanstatic import css_and_js
from kotti_ai.views import BaseView


@view_defaults(context=CustomContent, permission='view')
class CustomContentViews(BaseView):
    """ Views for :class:`kotti_ai.resources.CustomContent` """

    @view_config(name='view', permission='view',
                 renderer='kotti_ai:templates/custom-content-default.pt')
    def default_view(self):
        """ Default view for :class:`kotti_ai.resources.CustomContent`

        :result: Dictionary needed to render the template.
        :rtype: dict
        """

        return {
            'foo': _(u'bar'),
        }

    @view_config(name='alternative-view', permission='view',
                 renderer='kotti_ai:templates/custom-content-alternative.pt')
    def alternative_view(self):
        """ Alternative view for :class:`kotti_ai.resources.CustomContent`.
        This view requires the JS / CSS resources defined in
        :mod:`kotti_ai.fanstatic`.

        :result: Dictionary needed to render the template.
        :rtype: dict
        """

        css_and_js.need()

        return {
            'foo': _(u'bar'),
        }

from kotti_ai.fanstatic import css_and_js
from kotti_ai.resources import Poll


@view_defaults(context=Poll)
class PollViews(BaseView):
    """ Views for :class:`kotti_ai.resources.Poll` """

    @view_config(name='view', permission='view',
                 renderer='kotti_ai:templates/poll.pt')
    def poll_view(self):
        css_and_js.need()
        choices = self.context.values()
        all_votes = sum(choice.votes for choice in choices)
        return {
            'choices': choices,
            'all_votes': all_votes
            }

from kotti_ai.resources import Choice
from pyramid.httpexceptions import HTTPFound


@view_defaults(context=Choice)
class ChoiceViews(BaseView):
    """ Views for :class:`kotti_ai.resources.Choice` """

    @view_config(name='vote', permission='view')
    def vote_view(self):
        self.context.votes += 1
        self.request.session.flash(
                        u'You have just voted for the choice "{0}"'.format(
                                        self.context.title), 'info')

        return HTTPFound(
            location=self.request.resource_url(self.context.parent))


