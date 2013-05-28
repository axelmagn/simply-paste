from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'simply_paste.views.home', name='home'),
    # url(r'^simply_paste/', include('simply_paste.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # snippets root
    url(r'^', include('snippets.urls')),

    # legal pages
    url(r'^terms/$', TemplateView.as_view(template_name = "content/terms.html"),
        name="terms"),
    url(r'^privacy/$',
        TemplateView.as_view(template_name = "content/privacy.html"),
        name="privacy"
    ),
    # about page
    url(r'^about/$', TemplateView.as_view(template_name = "content/about.html"),
        name="about"),
)

if settings.STATIC_DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )
    urlpatterns += staticfiles_urlpatterns()
