from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^(\d+)/$', 'lists.views.view_list', name='view_list'),
    url(r'^new$', 'lists.views.new_list', name='new_list'),
    # Check why the following line causes a huge amount of errors
    url(r'^users/(.+)/$', 'lists.views.my_lists', name='my_lists'),
)
