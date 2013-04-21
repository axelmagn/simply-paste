from rest_framework import serializers
from snippets.models import Snippet

class SnippetSerializer(serializers.ModelSerializer):
    """
    Serializer for the snippet model

    """
    class Meta:
        model = Snippet
