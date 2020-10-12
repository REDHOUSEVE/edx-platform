from django.conf import settings
from django.utils.translation import ugettext_noop

from xmodule.tabs import TabFragmentViewMixin
from courseware.tabs import EnrolledTab


class XViewerTab(TabFragmentViewMixin, EnrolledTab):
    type = 'xviewer'
    name = 'xviewer'
    title = ugettext_noop('XVIEWER')
    is_movable = True
    is_default = True
    is_hideable = True
    fragment_view_name = 'openedx.features.xviewer.views.XViewerFragmentView'

    @classmethod
    def is_enabled(cls, course=None, user=None):
        """
        Returns true if this tab is enabled.
        """
        return settings.FEATURES.get('ENABLE_XVIEWER_TAB', False)

    @property
    def uses_bootstrap(self):
        """
        Returns true if this tab is rendered with Bootstrap.
        """
        return True
