from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import api, views

urlpatterns = patterns('',
        # main views
        url(r'^(?P<pk>[0-9]+)/$', views.SnippetRetrieveView.as_view(),
            name="snippet-retrieve"),
        url(r'^$', views.SnippetCreateView.as_view(),
            name="snippet-create"),

        # api
        url(r'^api/snippets/create/$', api.SnippetCreate.as_view(),
            name="snippet-create-api"),
        url(r'^api/snippets/(?P<pk>[0-9]+)/$', api.SnippetRetrieve.as_view(),
            name="snippet-retrieve-api"),
        url(r'^api/snippets/push/$', api.SnippetPush.as_view(),
            name="snippet-push-api"),
)

urlpatterns = format_suffix_patterns(urlpatterns)
