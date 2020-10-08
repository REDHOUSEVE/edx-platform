from edxmako.shortcuts import render_to_string
from web_fragments.fragment import Fragment

from openedx.core.djangoapps.plugin_api.views import EdxFragmentView


class SketchfabViewerFragmentView(EdxFragmentView):
    """
    Component implementation of the sketchfab viewer.
    """

    def render_to_fragment(self, request, course_id=None, **kwargs):
        """
        Render the sketchfab viewer to a fragment.

        Args:
            request: The Django request.
            course_id: The id of the course in question.

        Returns:
            Fragment: The fragment representing the sketchfab viewer
        """
        html = render_to_string('sketchfab_viewer/index.html', {})

        fragment = Fragment(html)
        self.add_fragment_resource_urls(fragment)
        return fragment
