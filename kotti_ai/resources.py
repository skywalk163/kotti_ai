# -*- coding: utf-8 -*-

"""
Created on 2022-09-03
:author:  ()
"""

from kotti.interfaces import IDefaultWorkflow
from kotti.resources import Content
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Unicode
from zope.interface import implementer

from kotti_ai import _


@implementer(IDefaultWorkflow)
class CustomContent(Content):
    """ A custom content type. """

    id = Column(ForeignKey('contents.id'), primary_key=True)
    custom_attribute = Column(Unicode(1000))

    type_info = Content.type_info.copy(
        name=u'CustomContent',
        title=_(u'CustomContent'),
        add_view=u'add_custom_content',
        addable_to=[u'Document'],
        selectable_default_views=[
            ("alternative-view", _(u"Alternative view")),
        ],
    )

    def __init__(self, custom_attribute=None, **kwargs):
        """ Constructor

        :param custom_attribute: A very custom attribute
        :type custom_attribute: unicode

        :param **kwargs: Arguments that are passed to the base class(es)
        :type **kwargs: see :class:`kotti.resources.Content`
        """

        super(CustomContent, self).__init__(**kwargs)

        self.custom_attribute = custom_attribute

class Poll(Content):
    id = Column(Integer(), ForeignKey('contents.id'), primary_key=True)

    type_info = Content.type_info.copy(
        name=u'Poll',
        title=u'Poll',
        add_view=u'add_poll',
        addable_to=[u'Document'],
    )

class Choice(Content):
    id = Column(Integer(), ForeignKey('contents.id'), primary_key=True)
    votes = Column(Integer())

    type_info = Content.type_info.copy(
        name=u'Choice',
        title=u'Choice',
        add_view=u'add_choice',
        addable_to=[u'Poll','AImage'],
    )

    def __init__(self, votes=0, **kwargs):
        super(Choice, self).__init__(**kwargs)
        self.votes = votes


# add for AIImage
from depot.fields.filters.thumbnails import WithThumbnailFilter
from kotti.resources import Content
from kotti.resources import SaveDataMixin
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from zope.interface import implementer

from kotti_ai import _
from kotti_ai.interfaces import AIImage


@implementer(AIImage)
class AImage(SaveDataMixin, Content):
    """Image is a specialized version of :class:`~kotti.resources.File`, that
    adds thumbnails and has different views.
    """

    #: Primary key column in the DB
    #: (:class:`sqlalchemy.types.Integer`)
    id = Column(Integer(), ForeignKey("contents.id"), primary_key=True)

    data_filters = (
        WithThumbnailFilter(size=(128, 128), format="PNG"),
        WithThumbnailFilter(size=(256, 256), format="PNG"),
    )

    type_info = Content.type_info.copy(
        name="AImage",
        title=_("AImage"),
        add_view="add_image",
        addable_to=["Document"],
        selectable_default_views=[],
        uploadable_mimetypes=[
            "image/*",
        ],
    )


