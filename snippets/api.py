from rest_framework import generics, views
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer



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



class SnippetPush(views.APIView):
    """
    Session-based Snipped posting endpoint

    Create/Update functionality, using sessions to resolve snippet id.

    """
    def post(self, request, format=None):
        # make sure id isn't already specified
        # figure out if we're creating or updating
        # if creating, call post from SnippetCreate
        # if updating
            # populate snippet id w/ cached session info
            # call post from SnippetUpdate

