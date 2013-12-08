import logging

from plone.i18n.normalizer.interfaces import IIDNormalizer
from plone.portlets.interfaces import IPortletDataProvider
from plone.app.form.widgets.wysiwygwidget import WYSIWYGWidget
from plone.app.portlets.portlets import base
from zope import schema
from zope.interface import implements
from zope.component import getUtility
from zope.formlib import form

from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone.portlet.static import PloneMessageFactory as _

logger = logging.getLogger('groupdocs.viewer_java')


class IGDViewer_javaPortlet(IPortletDataProvider):
    """A portlet which renders predefined static HTML.

    It inherits from IPortletDataProvider because for this portlet, the
    data that is being rendered and the portlet assignment itself are the
    same.
    """

    header = schema.TextLine(
        title=_(u"Portlet header"),
        description=_(u"Title of the GroupDocs Viewer for Java portlet"),
        required=True)

    url = schema.TextLine(
        title=_(u"Viewer for Java URL"),
        description=_(u"GroupDocs Viewer for Java URL"),
        required=True)

    use_http_handlers = schema.Bool(
        title=_(u"Use HTTP Handlers"),
        description=_(u"Use HTTP Handlers"),
        required=True,
        default=True)

    default_file_name = schema.TextLine(
        title=_(u"Default file name"),
        description=_(u"Default file name"),
        required=False)

    width = schema.TextLine(
        title=_(u"Width"),
        description=_(u"Width of the Viewer for Java"),
        required=True,
        default=u"100%")
        
    height = schema.TextLine(
        title=_(u"Height"),
        description=_(u"Height of the Viewer for Java"),
        required=True,
        default=u"600px")

    omit_border = schema.Bool(
        title=_(u"Omit portlet border"),
        description=_(u"Tick this box if you want to render the text above "
                      "without the standard header, border or footer."),
        required=True,
        default=False)

    footer = schema.TextLine(
        title=_(u"Portlet footer"),
        description=_(u"Text to be shown in the footer"),
        required=False)

    more_url = schema.ASCIILine(
        title=_(u"Details link"),
        description=_(u"If given, the header and footer "
                      "will link to this URL."),
        required=False)


class Assignment(base.Assignment):
    """Portlet assignment.

    This is what is actually managed through the portlets UI and associated
    with columns.
    """

    implements(IGDViewer_javaPortlet)

    header = _(u"title_gdviewer_java_portlet", default=u"GroupDocs Viewer for Java portlet")
    url = u""
    use_http_handlers = True
    default_file_name = u""
    width = u""
    height = u""
    omit_border = False
    footer = u""
    more_url = ''

    def __init__(self, header=u"", url=u"", use_http_handlers=True, default_file_name=u"", width=u"", height=u"", omit_border=False, footer=u"",
                 more_url=''):
        self.header = header
        self.url = url
        self.use_http_handlers = use_http_handlers
        self.default_file_name = default_file_name
        self.width = width
        self.height = height
        self.omit_border = omit_border
        self.footer = footer
        self.more_url = more_url

    @property
    def title(self):
        """This property is used to give the title of the portlet in the
        "manage portlets" screen. Here, we use the title that the user gave.
        """
        return self.header


class Renderer(base.Renderer):
    """Portlet renderer.

    This is registered in configure.zcml. The referenced page template is
    rendered, and the implicit variable 'view' will refer to an instance
    of this class. Other methods can be added and referenced in the template.
    """

    render = ViewPageTemplateFile('gdviewer_java.pt')

    def css_class(self):
        """Generate a CSS class from the portlet header
        """
        header = self.data.header
        normalizer = getUtility(IIDNormalizer)
        return "portlet-static-%s" % normalizer.normalize(header)

    def has_link(self):
        return bool(self.data.more_url)

    def has_footer(self):
        return bool(self.data.footer)

    def transformed(self, mt='text/x-html-safe'):
        """Transform imput data to get iframe code for GroupDocs Embedded Viewer_java.
        """
        frame_source = '<script type="text/javascript" src="{url}/assets/js/libs/jquery-1.9.1.min.js"></script>\r\n' \
                       '<script type="text/javascript" src="{url}/assets/js/libs/jquery-ui-1.10.3.min.js"></script>\r\n' \
                       '<script type="text/javascript" src="{url}/assets/js/libs/knockout-2.2.1.js"></script>\r\n' \
                       '<script type="text/javascript" src="{url}/assets/js/libs/turn.min.js"></script>\r\n' \
                       '<script type="text/javascript" src="{url}/assets/js/libs/modernizr.2.6.2.Transform2d.min.js"></script>\r\n' \
                       '<script type="text/javascript">\r\n' \
                       '    if (!window.Modernizr.csstransforms) {\r\n' \
                       '        var scriptLoad = document.createElement("script");\r\n' \
                       '        scriptLoad.setAttribute("type", "text/javascript");\r\n' \
                       '        scriptLoad.setAttribute("src", "{url}/assets/js/libs/turn.html4.min.js");\r\n' \
                       '        document.getElementsByTagName("head")[0].appendChild(scriptLoad);\r\n' \
                       '    }\r\n' \
                       '</script>\r\n' \
                       '<script type="text/javascript" src="{url}/assets/js/installableViewer.min.js"></script>\r\n' \
                       '<script type="text/javascript">\r\n' \
                       '    $.fn.groupdocsViewer.prototype.applicationPath = "{url}/";\r\n' \
                       '</script>\r\n' \
                       '<script type="text/javascript">\r\n' \
                       '    $.fn.groupdocsViewer.prototype.useHttpHandlers = {use_http_handlers};\r\n' \
                       '</script>\r\n' \
                       '<script type="text/javascript" src="{url}/assets/js/GroupdocsViewer.all.min.js"></script>\r\n' \
                       '<link rel="stylesheet" type="text/css" href="{url}/assets/css/bootstrap.css">\r\n' \
                       '<link rel="stylesheet" type="text/css" href="{url}/assets/css/GroupdocsViewer.all.min.css">\r\n' \
                       '<link rel="stylesheet" type="text/css" href="{url}/assets/css/jquery-ui-1.10.3.dialog.min.css">\r\n' \
                       '<style type="text/css">\r\n' \
                       '    #java_groupdocs_viewer p\r\n' \
                       '    {\r\n' \
                       '        color: #737373;\r\n' \
                       '    }</style>\r\n' \
                       '<div id="java_groupdocs_viewer" style="width: {width}; height: {height}; overflow: hidden; position: relative;    margin-bottom: 20px; background-color: gray; border: 1px solid #ccc;"></div>\r\n' \
                       '<script type="text/javascript">\r\n' \
                       '    $(function () {\r\n' \
                       '        var localizedStrings = null;\r\n' \
                       '        var thumbsImageBase64Encoded = null;\r\n' \
                       '        $("#java_groupdocs_viewer").groupdocsViewer({\r\n' \
                       '            filePath: "{default_file_name}",\r\n' \
                       '            docViewerId: "doc_viewer1",\r\n' \
                       '            quality: 100,\r\n' \
                       '            showHeader: true,\r\n' \
                       '            showThumbnails: true,\r\n' \
                       '            openThumbnails: true,\r\n' \
                       '            initialZoom: 100,\r\n' \
                       '            zoomToFitWidth: true,\r\n' \
                       '            zoomToFitHeight: false,\r\n' \
                       '            backgroundColor: "",\r\n' \
                       '            showFolderBrowser: true,\r\n' \
                       '            showPrint: true,\r\n' \
                       '            showDownload: true,\r\n' \
                       '            showZoom: true,\r\n' \
                       '            showPaging: true,\r\n' \
                       '            showViewerStyleControl: true,\r\n' \
                       '            showSearch: true,\r\n' \
                       '            preloadPagesCount: 0,\r\n' \
                       '            viewerStyle: 1,\r\n' \
                       '            supportTextSelection: true,\r\n' \
                       '            localizedStrings: localizedStrings,\r\n' \
                       '            thumbsImageBase64Encoded: thumbsImageBase64Encoded,\r\n' \
                       '            showDownloadErrorsInPopup: true\r\n' \
                       '        });\r\n' \
                       '    });\r\n' \
                       '</script>'

        return frame_source\
            .replace('{url}', self.data.url)\
            .replace('{use_http_handlers}', str(self.data.use_http_handlers).lower())\
            .replace('{width}', self.data.width)\
            .replace('{height}', self.data.height)\
            .replace('{default_file_name}', self.data.default_file_name or '')


class AddForm(base.AddForm):
    """Portlet add form.

    This is registered in configure.zcml. The form_fields variable tells
    zope.formlib which fields to display. The create() method actually
    constructs the assignment that is being added.
    """
    form_fields = form.Fields(IGDViewer_javaPortlet)
    label = _(u"title_add_viewer_java_portlet",
              default=u"Add groupdocs Viewer for Java portlet")
    description = _(u"description_viewer_java_portlet",
                    default=u"A portlet which can display Embedded GroupDocs Viwer for Java.")

    def create(self, data):
        return Assignment(**data)


class EditForm(base.EditForm):
    """Portlet edit form.

    This is registered with configure.zcml. The form_fields variable tells
    zope.formlib which fields to display.
    """
    form_fields = form.Fields(IGDViewer_javaPortlet)
    label = _(u"title_edit_viewer_java_portlet",
              default=u"Edit GroupDocs Viewer for Java portlet")
    description = _(u"description_viewer_java_portlet",
                    default=u"A portlet which can display Embedded GroupDocs Viwer for Java.")
