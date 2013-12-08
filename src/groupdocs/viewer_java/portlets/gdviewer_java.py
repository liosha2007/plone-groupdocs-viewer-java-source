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
        description=_(u"Title of the GroupDocs Viewer_java portlet"),
        required=True)

    formid = schema.TextLine(
        title=_(u"Form ID"),
        description=_(u"Form ID from GroupDocs account"),
        required=True)
        
    width = schema.TextLine(
        title=_(u"Width"),
        description=_(u"Width of the Viewer_java"),
        required=True)
        
    height = schema.TextLine(
        title=_(u"Height"),
        description=_(u"Height of the Viewer_java"),
        required=True)

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

    header = _(u"title_gdviewer_java_portlet", default=u"GroupDocs Viewer_java portlet")
    formid = u""
    width = u""
    height = u""
    omit_border = False
    footer = u""
    more_url = ''

    def __init__(self, header=u"", formid=u"", width=u"", height=u"", omit_border=False, footer=u"",
                 more_url=''):
        self.header = header
        self.formid = formid
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
        frame_source = '<iframe src="https://apps.groupdocs.com/viewer_java2/forms/SignEmbed/' + self.data.formid + '?referer=Plone-Viewer_java/1.0.3" frameborder="0" width="' + self.data.width + '" height="' + self.data.height + '">If you can see this text, your browser does not support iframes. Please enable iframe support in your browser or use the latest version of any popular web browser such as Mozilla Firefox or Google Chrome. For more help, please check our documentation Wiki: <a href="http://groupdocs.com/docs/display/viewer_java/GroupDocs+Viewer_java+Integration+with+3rd+Party+Platforms">http://groupdocs.com/docs/display/viewer_java/GroupDocs+Viewer_java+Integration+with+3rd+Party+Platforms</a></iframe>'

        if frame_source:
            return frame_source
        return None


class AddForm(base.AddForm):
    """Portlet add form.

    This is registered in configure.zcml. The form_fields variable tells
    zope.formlib which fields to display. The create() method actually
    constructs the assignment that is being added.
    """
    form_fields = form.Fields(IGDViewer_javaPortlet)
    label = _(u"title_add_viewer_java_portlet",
              default=u"Add groupdocs viewer_java portlet")
    description = _(u"description_viewer_java_portlet",
                    default=u"A portlet which can display GroupDocs Embedded Viwer.")

    def create(self, data):
        return Assignment(**data)


class EditForm(base.EditForm):
    """Portlet edit form.

    This is registered with configure.zcml. The form_fields variable tells
    zope.formlib which fields to display.
    """
    form_fields = form.Fields(IGDViewer_javaPortlet)
    label = _(u"title_edit_viewer_java_portlet",
              default=u"Edit GroupDocs Viewer_java portlet")
    description = _(u"description_viewer_java_portlet",
                    default=u"A portlet which can display GroupDocs Embedded Viwer.")
