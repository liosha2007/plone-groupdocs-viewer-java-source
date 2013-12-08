from zope.i18nmessageid import MessageFactory
PloneMessageFactory = MessageFactory('plone')

from Products.CMFCore.permissions import setDefaultRoles
setDefaultRoles('viewer_java.portlets.gdviewer_java: Add GroupDocs Viewer_java portlet',
                ('Manager', 'Site Administrator', 'Owner',))
