from edxmako.shortcuts import render_to_string
from web_fragments.fragment import Fragment

from openedx.core.djangoapps.plugin_api.views import EdxFragmentView


class TournamentsFragmentView(EdxFragmentView):
    """
    Component implementation of the Tournaments viewer.
    """

    def render_to_fragment(self, request, course_id=None, **kwargs):
        """
        Render the Tournament viewer to a fragment.

        Args:
            request: The Django request.
            course_id: The id of the course in question.

        Returns:
            Fragment: The fragment representing the Tournament viewer
        """
        html = render_to_string('tournaments/index.html', {})

        fragment = Fragment(html)
        self.add_fragment_resource_urls(fragment)
        return fragment
