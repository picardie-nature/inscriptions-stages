from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'inscription_stages_initations.views.home', name='home'),
	# url(r'^inscription_stages_initations/', include('inscription_stages_initations.foo.urls')),

	# Uncomment the admin/doc line below to enable admin documentation:
	# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'inscriptions.views.stage_perf'),
	#url(r'^$', 'inscriptions.views.index'),
	url(r'^merci/', 'inscriptions.views.merci'),
	url(r'^merci_perf/', 'inscriptions.views.merci_perf'),
	url(r'^stage_perf/', 'inscriptions.views.stage_perf'),
	url(r'^stage_init/', 'inscriptions.views.index')
)
