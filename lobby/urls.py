from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(r'^$', 'lobby.wholobbiesus.views.index'),
	(r'^index$', 'lobby.wholobbiesus.views.index'),
	(r'^about$', 'lobby.wholobbiesus.views.about'),
	(r'^detail/(\d+)', 'lobby.wholobbiesus.views.detail'),
	(r'^issues/$', 'lobby.wholobbiesus.views.issue_list'),
	(r'^issue/$', 'lobby.wholobbiesus.views.issue_list'),
	(r'^issue/(.*)', 'lobby.wholobbiesus.views.issue_detail'),
	(r'^filing/(.*)\/xml', 'lobby.wholobbiesus.views.filing_xml'),
	(r'^filing/(.*)', 'lobby.wholobbiesus.views.filing'),
	(r'^registrant/(.*)', 'lobby.wholobbiesus.views.registrant_detail'),
	(r'^client/(.*)', 'lobby.wholobbiesus.views.client_detail'),
	(r'^agency/(.*)', 'lobby.wholobbiesus.views.agency_detail'),	
	(r'^lobbyist/(.*)', 'lobby.wholobbiesus.views.lobbyist_detail'),
	(r'^search/', 'lobby.wholobbiesus.views.search'),	
)
