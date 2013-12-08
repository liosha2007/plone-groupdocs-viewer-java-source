.. contents::

GroupDocs Viewer_java plugin for Plone
=============================

This plugin is developed by the GroupDocs marketplace team. It allows you to easily integrate the GroupDocs Viewer_java app into your Plone website. With this application, you can easily embed business documents, such as contracts and invoices into your Plon web pages and then send them to your partners/clients so that they can sign the documents online, from their web browsers. This way you can easily [collect viewer_javas online](http://groupdocs.com/apps/viewer_java), without the need of printing, scanning and faxing them.   

###Plugin installation steps:

If the plugin is only available on GitHub (not released to PyPi yet), it can be installed with a build-out by following these steps:

* Create a groupdocs.viewer_java directory under the C:\Plone42\src\ folder.
* Download the plugin files from GitHub into the folder created.
* Change the buildout.cfg file as following: 1. Add the “groupdocs.viewer_java” record into the "eggs =" section. 2. Add the “src/groupdocs.viewer_java” record into the "develop =" section.
* Run the buildout .\bin\buildout.exe file from within the Plone installation folder (For example, C:\Plone42).
* Restart Plone.
* Go to Admin->Site setup (http://localhost:8080/PloneGD/@@overview-controlpanel)
* Open the Add-ons section:  http://localhost:8080/PloneGD/prefs_install_products_form
* Find the GroupDocs Viewer_java 1.0 add-on, then check and activate it.

###Using plugin:
* Modify or create a new page
* Click on the “Manage Portlets” link: http://screencast.com/t/fbjWrqCJuCfP 
* Click on the “Add portlet...” dropbox and select the GroupDocs Viewer_java portlet: http://screencast.com/t/fAAlxv1dL 
* Configure portlet's parameters and press the “Save” button: http://screencast.com/t/zJW3kiyMrW 
* Open the created page (http://localhost:8080/PloneGD/gd-test). GroupDocs Viewer should appear in the portlet region now: http://screencast.com/t/VMd3UZc5 

###[Sign, Manage, Annotate, Assemble, Compare and Convert Documents with GroupDocs](http://groupdocs.com)
1. [Sign documents online with GroupDocs Viewer_java](http://groupdocs.com/apps/viewer_java)
2. [PDF, Word and Image Annotation with GroupDocs Annotation](http://groupdocs.com/apps/annotation)
3. [Online DOC, DOCX, PPT Document Comparison with GroupDocs Comparison](http://groupdocs.com/apps/comparison)
4. [Online Document Management with GroupDocs Dashboard](http://groupdocs.com/apps/dashboard)
5. [Doc to PDF, Doc to Docx, PPT to PDF, and other Document Conversions with GroupDocs Viewer](http://groupdocs.com/apps/viewer)
6. [Online Document Automation with GroupDocs Assembly](http://groupdocs.com/apps/assembly)

###Created by [GroupDocs Marketplace Team]( http://groupdocs.com/marketplace/ ).
