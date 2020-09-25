"""
Contains waffle switches related to redhouse panel.
"""
from openedx.core.djangoapps.waffle_utils import WaffleSwitchNamespace

# Namespace
WAFFLE_NAMESPACE = 'redhouse_panel'

# Switches
ENABLE_REDHOUSE_PANEL = 'enable_redhouse_panel'


def waffle():
    """
    Returns the namespaced, cached, audited Waffle class for Redhouse Panel.
    """
    return WaffleSwitchNamespace(name=WAFFLE_NAMESPACE, log_prefix='Redhouse Panel: ')
