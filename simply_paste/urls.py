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

    url(r'^terms/$', 'assets.views.TermsView', name="terms"),
    url(r'^privacy/$', 'assets.views.PrivacyView', name="privacy"),
    url(r'^about/$', 'assets.views.AboutView', name="about"),
)

if settings.STATIC_DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )
    urlpatterns += staticfiles_urlpatterns()
