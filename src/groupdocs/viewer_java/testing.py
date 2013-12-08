from plone.app.testing import PloneWithPackageLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

import groupdocs.viewer_java


GROUPDOCS_VIEWER = PloneWithPackageLayer(
    zcml_package=groupdocs.viewer_java,
    zcml_filename='testing.zcml',
    gs_profile_id='groupdocs.viewer_java:testing',
    name="GROUPDOCS_VIEWER")

GROUPDOCS_VIEWER_INTEGRATION = IntegrationTesting(
    bases=(GROUPDOCS_VIEWER, ),
    name="GROUPDOCS_VIEWER_INTEGRATION")

GROUPDOCS_VIEWER_FUNCTIONAL = FunctionalTesting(
    bases=(GROUPDOCS_VIEWER, ),
    name="GROUPDOCS_VIEWER_FUNCTIONAL")
