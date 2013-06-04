from rest_framework import generics, views, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from snippets.models import Snippet, LANGUAGE_CHOICES
from snippets.serializers import SnippetSerializer
from snippets.settings import SESSION_SNIPPET_ID
import pdb # DEBUG



@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'snippet-push'  : reverse('snippet-push-api', request=request,
                                  format=format),
        'snippet-create': reverse('snippet-create-api', request=request,
                                  format=format)
    })


class SnippetList(generics.ListAPIView):
    """RESTful list for Snippet Model"""
    model = Snippet
    serializer_class = SnippetSerializer



class SnippetCreate(generics.CreateAPIView):
    """RESTful create for Snippet Model"""
    model = Snippet
    serializer_class = SnippetSerializer



class SnippetUpdate(generics.UpdateAPIView):
    """RESTful update for Snippet Model"""
    # TODO: session auth
    model = Snippet
    serializer_class = SnippetSerializer



class SnippetRetrieve(generics.RetrieveAPIView):
    """RESTful retrieve for Snippet Model"""
    model = Snippet
    serializer_class = SnippetSerializer



class SnippetPush(SnippetUpdate,
                  mixins.CreateModelMixin):
    """
    Session-based Snipped posting endpoint

    Create/Update functionality, using sessions to resolve snippet id.

    """
    model = Snippet
    serializer_class = SnippetSerializer

    def post(self, request, *args, **kwargs):
        # figure out if we're creating or updating
        snippet_id = request.session.get(SESSION_SNIPPET_ID)
        snippet_is_new = snippet_id == None
        # if creating, call post from SnippetCreate
        if snippet_is_new:
            response = self.create(request, *args, **kwargs)
            request.session[SESSION_SNIPPET_ID] = response.data['uuid']
            return response
        # if updating
        else:
            # overwrite snippet id w/ cached session info
            self.kwargs[self.pk_url_kwarg] = snippet_id
            # call post from SnippetUpdate
            return self.update(request, *args, **kwargs)

class SnippetLanguageChoices(views.APIView):
    """
    Return the different language choices available to a snippet

    """
    def get(self, request, *args, **kwargs):
        return Response(LANGUAGE_CHOICES);
