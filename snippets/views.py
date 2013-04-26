from rest_framework import renderers, generics
from rest_framework.response import Response
from snippets.models import Snippet
from snippets.settings import SESSION_SNIPPET_ID

class SnippetRetrieveView(generics.RetrieveAPIView):
    """
    Highlighted snippet code.

    """
    model = Snippet
    renderer_classes = (renderers.TemplateHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(
                {'snippet': snippet},
                template_name='snippets/retrieve.html'
        )


class SnippetCreateView(generics.CreateAPIView):
    """
    Create a snippet of code.

    """
    model = Snippet
    renderer_classes = (renderers.TemplateHTMLRenderer,)
    def get(self, request, *args, **kwargs):
        request.session[SESSION_SNIPPET_ID] = None
        return Response(template_name='snippets/create.html')

