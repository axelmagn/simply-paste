from rest_framework import generics, views, mixins
from rest_framework.response import Response
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
import pdb # DEBUG

# session key for currently active snippet
SESSION_SNIPPET_ID = 'snippet_id'


class SnippetCreate(generics.CreateAPIView):
    """Standard RESTful create for Snippet Model"""
    model = Snippet
    serializer_class = SnippetSerializer



class SnippetUpdate(generics.UpdateAPIView):
    """Standard RESTful update for Snippet Model"""
    # TODO: session auth
    model = Snippet
    serializer_class = SnippetSerializer



class SnippetRetrieve(generics.RetrieveAPIView):
    """Standard RESTful retrieve for Snippet Model"""
    model = Snippet
    serializer_class = SnippetSerializer



class SnippetPush(generics.GenericAPIView,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin):
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
            request.session[SESSION_SNIPPET_ID] = response.data['id']
            return response
        # if updating
        else:
            # populate snippet id w/ cached session info
            # TODO: request.DATA is immutable.  Must create copy. BUG
            request.DATA['id'] = snippet_id
            # call post from SnippetUpdate
            return self.update(self, request, *args, **kwargs)
