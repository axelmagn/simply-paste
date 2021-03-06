from rest_framework import serializers
from snippets.models import Snippet

class SnippetSerializer(serializers.ModelSerializer):
    """
    Serializer for the snippet model

    """
    # api url
    url = serializers.HyperlinkedIdentityField(
            view_name="snippet-retrieve-api",
    )

    #
    display_url = serializers.HyperlinkedIdentityField(
            view_name="snippet-retrieve",
            format='html'
    )

    lookup_field='uuid'

    class Meta:
        model = Snippet
        read_only_fields = ('created',)
