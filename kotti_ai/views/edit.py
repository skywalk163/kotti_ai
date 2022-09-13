# -*- coding: utf-8 -*-

"""
Created on 2022-09-03
:author:  ()
"""

import colander
from kotti.views.edit import ContentSchema
from kotti.views.form import AddFormView
from kotti.views.form import EditFormView
from pyramid.view import view_config

from kotti_ai import _
from kotti_ai.resources import CustomContent

import cv2

class CustomContentSchema(ContentSchema):
    """ Schema for CustomContent. """

    custom_attribute = colander.SchemaNode(
        colander.String(),
        title=_(u"Custom attribute"))


@view_config(name=CustomContent.type_info.add_view,
             permission=CustomContent.type_info.add_permission,
             renderer='kotti:templates/edit/node.pt')
class CustomContentAddForm(AddFormView):
    """ Form to add a new instance of CustomContent. """

    schema_factory = CustomContentSchema
    add = CustomContent
    item_type = _(u"CustomContent")


@view_config(name='edit', context=CustomContent, permission='edit',
             renderer='kotti:templates/edit/node.pt')
class CustomContentEditForm(EditFormView):
    """ Form to edit existing CustomContent objects. """

    schema_factory = CustomContentSchema


   
class PollSchema(ContentSchema):
    """Schema for Poll"""

    title = colander.SchemaNode(
        colander.String(),
        title=_(u'Question'),
    )


class ChoiceSchema(ContentSchema):
    """Schema for Choice"""

    title = colander.SchemaNode(
        colander.String(),
        title=_(u'Choice'),
    )


from kotti_ai.resources import Choice
from kotti_ai.resources import Poll


@view_config(name='edit', context=Poll, permission='edit',
             renderer='kotti:templates/edit/node.pt')
class PollEditForm(EditFormView):
    schema_factory = PollSchema


@view_config(name=Poll.type_info.add_view, permission='add',
             renderer='kotti:templates/edit/node.pt')
class PollAddForm(AddFormView):
    schema_factory = PollSchema
    add = Poll
    item_type = u"Poll"


@view_config(name='edit', context=Choice, permission='edit',
             renderer='kotti:templates/edit/node.pt')
class ChoiceEditForm(EditFormView):
    schema_factory = ChoiceSchema


@view_config(name=Choice.type_info.add_view, permission='add',
             renderer='kotti:templates/edit/node.pt')
class ChoiceAddForm(AddFormView):
    schema_factory = ChoiceSchema
    add = Choice
    item_type = u"Choice"
    # from kotti_ai.ppshitu  import ppshitu
    # ppshitu()

 

## add AImage
from pyramid.view import view_config

from kotti.views.edit.content import FileEditForm, FileAddForm

from kotti_ai import _
from kotti_ai.resources import AImage


@view_config(
    name=AImage.type_info.add_view,
    permission=AImage.type_info.add_permission,
    renderer="kotti:templates/edit/node.pt",
)
class AImageAddForm(FileAddForm):
    item_type = _("AImage")
    item_class = AImage


@view_config(
    name="edit",
    context=AImage,
    permission="edit",
    renderer="kotti:templates/edit/node.pt",
)
class AImageEditForm(FileEditForm):
    # # 学习渲染视图里添加一个链接到菜单
    # @view_config(
    #     name="my-custom-submenu", permission="edit",
    #     renderer="kotti_ai:templates/my-custom-submenu.pt")
    # def my_custom_submenu(context, request):
    #     return {}
    pass

# 学习渲染视图里添加一个链接到菜单
@view_config(
    name="my-custom-submenu", permission="edit",
    renderer="kotti_ai:templates/my-custom-submenu.pt")
def my_custom_submenu(context, request):
    from kotti_ai.ppshitu  import ppshitu
    print("context.description", context.description)
    print(dir(context))
    print(dir(request))
    print(context.keys())
    # print(context.metadata) # MetaData(bind=Engine(sqlite:////home/pyramid/work/kotti_ai/kotti_ai.db))
    # print(request.resource_url(context, 'image')) # http://web.airoot.org:5000/test3/image
    # # print(context.from_field_storage)
    # print("type of :", type(context.data.file.read()))
    # print(context.data.file.read()[:300])
    # print(context.data.file.read()[:300].decode('utf8'))
    # import numpy as np
    # im = np.frombuffer(context.data.file.read(), np.uint8)
    # print("type of im:", type(im))
    # for i in dir(context) :
    #     print(i, context[i])
    #     print(eval("context." + i))
    print("====context.description", context.description)
    # for i in context.keys():
    #     print(i, context.items(i))
    print("====context.title", context.title, type(context), context.__class__)
    print("==== isinstance(context, AImage) :",  isinstance(context, AImage))
    # if context.__class__ != AImage.__class__ :
    if not isinstance(context, AImage) :
        print("====context.__class__ != AImage.__class__ :", False)
        return {}
    # if context.description == None or context.description[:2] != "[{":
    if  context.description[:1] != "[":
        print("====AImage start")
        print("====context.filename", context.filename) # 没有context.minetype
        print("====context.size", context.size)
        print("====len of context.data", len(context.data))
        print("====type of context.data", type(context.data))
        print("====context.from_field_storage", type(context.from_field_storage))
        print(dir(context.from_field_storage))
        # print(context.from_field_storage())
        # print(context.data[0], context.data[1])
        im = None
        print("context.keys()", context.keys())
        # if "data" in context.keys() :
        if "data" in dir(context) :
            # from plone.scale.scale import scaleImage
            import numpy as np
            # width = 256
            # height = 256 
            # image, format, size = scaleImage(
            # context.data.file.read(), width=width, height=height, mode="contain")
                                            
            # print("====size", size, "type(image):", type(image))
            # print("====image.shape:", np.frombuffer(image, np.uint8).shape)
            tmpdata = context.data.file.read()
            print("====len of tmpdata", len(tmpdata))
            image = cv2.imdecode(np.fromstring(tmpdata, np.uint8), 1)
            print("====image", image.shape)
            im = image
            # im = cv2.imdecode(tmpdata)
            # print("type of im", type(im), len(im))
            # if tmpdata !=None :
            #     import numpy as np
            #     im = np.frombuffer(tmpdata, np.uint8)
            #     print("im.shape:", im.shape)
            #     if im.shape[0] !=3 :
            #         return {}
            out = ppshitu(im=im)
            print("====out:", out)
            context.description = str(out)
    return {}

# @view_config(
#     name="my-custom-submenu", permission="edit",
#     renderer="kotti_ai:templates/image.pt")
# def my_custom_submenu(context, request):
#     from kotti_ai.ppshitu  import ppshitu
#     out = ppshitu(im=None)
#     print("=="*20, out)
#     # context.description = out
#     return {}

# @view_config(
#     name="my-custom-submenu", permission="edit",
#     renderer="kotti_ai:templates/my-custom-submenu.pt")
# def my_custom_submenu(context, request):
#     from kotti_ai.ppshitu  import ppshitu
#     out = ppshitu(im=None)
#     context.description = out
#     return {}

# @view_config(
#     name="my-custom-submenu",
#     context=AImage,
#     permission="edit",
#     renderer="kotti:templates/edit/node.pt",
# )
# class my_custom_submenu(FileEditForm):
#     # # 学习渲染视图里添加一个链接到菜单
#     # @view_config(
#     #     name="my-custom-submenu", permission="edit",
#     #     renderer="kotti_ai:templates/my-custom-submenu.pt")
#     # def my_custom_submenu(context, request):
#     #     return {}
#     from kotti_ai.ppshitu  import ppshitu
#     out = ppshitu(im=None)
#     self.context.descriptioncon = str(out)
    # pass