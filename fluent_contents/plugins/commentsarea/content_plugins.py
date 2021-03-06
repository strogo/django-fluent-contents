"""
Comments area plugin.

This plugin package is not called "comments" as that conflicts
with the `django.contrib.comments` appname. Hence, "commentsarea" it is.

The plugin displays the form and messagelist that ``django.contrib.comments`` renders.
Hence, it depends on a properly configured contrib module.
The least you need to do, is:

  * providing a ``comments/base.html`` template.
   * include a ``title`` block that is displayed in the ``<head>`` of the base template.
   * include a ``content`` block that is displayed in the ``<body>`` of the base template.
  * provide a ``comments/posted.html`` template for the success page.
   * It could contains links to the blog page.
   * It could redirect automatically back to the blog in a few seconds.
"""
from django.utils.translation import ugettext_lazy as _
from fluent_contents.extensions import ContentPlugin, plugin_pool
from fluent_contents.plugins.commentsarea.models import CommentsAreaItem


class CommentsAreaPlugin(ContentPlugin):
    model = CommentsAreaItem
    category = _('Interactivity')
    render_template = "fluent_contents/plugins/commentsarea/commentsarea.html"


plugin_pool.register(CommentsAreaPlugin)
