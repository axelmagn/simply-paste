from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import api

urlpatterns = patterns('',
    url(r'^api/snippets/create/$', api.SnippetCreate.as_view()),
    url(r'^api/snippets/(?P<pk>[0-9]+)/$', api.SnippetRetrieve.as_view()),
    url(r'^api/snippets/push/$', api.SnippetPush.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)
