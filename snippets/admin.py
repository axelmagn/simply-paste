from django.contrib import admin
from snippets.models import Snippet

class SnippetAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'created', 'language')

admin.site.register(Snippet, SnippetAdmin)
