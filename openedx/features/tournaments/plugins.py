from django.conf import settings
from django.utils.translation import ugettext_noop

from xmodule.tabs import TabFragmentViewMixin
from courseware.tabs import EnrolledTab
from openedx.core.djangoapps.site_configuration import helpers as configuration_helpers


class TournamentsTab(TabFragmentViewMixin, EnrolledTab):
    type = 'tournaments'
    name = 'tournaments'
    title = ugettext_noop('Tournaments')
    is_movable = True
    is_default = True
    is_hideable = True
    fragment_view_name = 'openedx.features.tournaments.views.TournamentsFragmentView'

    @classmethod
    def is_enabled(cls, course=None, user=None):
        """
        Returns true if this tab is enabled.
        """
        is_enabled = super(TournamentsTab, cls).is_enabled(course, user)
        return configuration_helpers.get_value("ENABLE_TOURNAMENTS_TAB", False) and is_enabled

    @property
    def uses_bootstrap(self):
        """
        Returns true if this tab is rendered with Bootstrap.
        """
        return True
