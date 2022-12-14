# -*- coding: utf-8 -*-

"""
Created on 2022-09-03
:author:  ()
"""


class BaseView(object):
    """ Base class for views """

    def __init__(self, context, request):
        """ Constructor

        :param context: Context of the view
        :type context: :class:`kotti.resources.Content`

        :param request: Current request
        :type request: :class:`kotti.request.Request`
        """

        super(BaseView, self).__init__()

        self.context = context
        self.request = request

        
# for AImage
import PIL
from depot.utils import make_content_disposition
from kotti.util import extract_from_settings
from plone.scale.scale import scaleImage
from pyramid.response import Response
from pyramid.view import view_config
from pyramid.view import view_defaults

from kotti_ai.interfaces import AIImage

PIL.ImageFile.MAXBLOCK = 33554432

#: Default image scales
image_scales = {
    "span1": [60, 120],
    "span2": [160, 320],
    "span3": [260, 520],
    "span4": [360, 720],
    "span5": [460, 920],
    "span6": [560, 1120],
    "span7": [660, 1320],
    "span8": [760, 1520],
    "span9": [860, 1720],
    "span10": [960, 1920],
    "span11": [1060, 2120],
    "span12": [1160, 2320],
}


@view_defaults(context=AIImage, permission="view")
class AImageView(object):
    """The ImageView class is registered for the :class:`AIImage` context."""

    def __init__(self, context, request):

        self.context = context
        self.request = request

    @view_config(name="view", renderer="kotti_ai:templates/image.pt")
    def view(self):
        """
        :result: Empty dictionary to be handed to the image.pt template for
                 rendering.
        :rtype: dict
        """

        return {}

    @view_config(name="image")
    def image(self, subpath=None):
        """Return the image in a specific scale, either inline
        (default) or as attachment.
        :param subpath: [<image_scale>]/download] (optional).
                        When 'download' is the last element in subpath,
                        the image is served with a 'Content-Disposition:
                        attachment' header.  <image_scale> has to be one of the
                        predefined image_scales - either from the defaults in
                        this module or one set with a
                        kotti.image_scales.<scale_name> in your app config ini
                        file.
        :type subpath: str
        :result: complete response object
        :rtype: pyramid.response.Response
        """

        if subpath is None:
            subpath = self.request.subpath

        width, height = (None, None)
        subpath = list(subpath)

        if (len(subpath) > 0) and (subpath[-1] == "download"):
            disposition = "attachment"
            subpath.pop()
        else:
            disposition = "inline"

        if len(subpath) == 1:
            scale = subpath[0]
            if scale in image_scales:
                # /path/to/image/scale/thumb
                width, height = image_scales[scale]

        if not (width and height):
            return self.request.uploaded_file_response(self.context.data, disposition)

        image, format, size = scaleImage(
            self.context.data.file.read(), width=width, height=height, mode="contain"
        )
        res = Response(
            headerlist=[
                (
                    "Content-Disposition",
                    '{0};filename="{1}"'.format(
                        disposition, self.context.filename.encode("ascii", "ignore")
                    ),
                ),
                ("Content-Length", str(len(image))),
                ("Content-Type", str(self.context.mimetype)),
            ],
            body=image,
        )
        # res.content_disposition = rfc6266_parser.build_header(
        #     self.context.filename, disposition=disposition,
        #     filename_compat=unidecode(self.context.filename))
        res.content_disposition = make_content_disposition(
            disposition, self.context.filename
        )

        return res
    
    # # ????????????????????????????????????????????????
    # @view_config(
    #     name="my-custom-submenu", permission="edit",
    #     renderer="kotti_ai:templates/my-custom-submenu.pt")
    # def my_custom_submenu(context=self.context, request=self.request):
    #     return {}


def _load_image_scales(settings):
    image_scale_strings = extract_from_settings("kotti.image_scales.", settings)

    for k in image_scale_strings.keys():
        image_scales[k] = [int(x) for x in image_scale_strings[k].split("x")]


# def includeme(config):
#     _load_image_scales(config.registry.settings)

#     config.scan(__name__)
    
# # ????????????????????????????????????????????????
# @view_config(
#     name="my-custom-submenu", permission="edit",
#     renderer="kotti_ai:templates/my-custom-submenu.pt")
# def my_custom_submenu(context, request):
#     return {}