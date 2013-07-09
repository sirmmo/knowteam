from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

	url(r'', include('social_auth.urls')),
    # Examples:
    url(r'^$', 					'core.views.index', name='home'),
    url(r'^user$', 				'core.views.user', name='users'),
    url(r'^user/(?P<id>\w+)$', 	'core.views.user', name='user'),
    url(r'^team$', 				'core.views.team', name='teams'),
    url(r'^team/(?P<id>\w+)$', 	'core.views.team', name='team'),
    # url(r'^knowteam/', include('knowteam.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
