"""
ACE message types for the redhouse panel.
"""

from openedx.core.djangoapps.ace_common.message import BaseMessageType


class PasswordSet(BaseMessageType):
    def __init__(self, *args, **kwargs):
        super(PasswordSet, self).__init__(*args, **kwargs)
