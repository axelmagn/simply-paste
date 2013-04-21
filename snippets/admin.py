from django.contrib import admin
from snippets.models import Snippet

class SnippetAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'language')

admin.site.register(Snippet, SnippetAdmin)
