from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from assets.views import AboutView, PrivacyView, TermsView

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

    url(r'^terms/$', TermsView.as_view(), name="terms"),
    url(r'^privacy/$', PrivacyView.as_view(), name="privacy"),
    url(r'^about/$', AboutView.as_view(), name="about"),

    # snippets root
    url(r'^', include('snippets.urls')),

)

if settings.STATIC_DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )
    urlpatterns += staticfiles_urlpatterns()
