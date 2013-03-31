from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from apps.views import review, item_filter, review_all

urlpatterns = patterns('',
        url(r'^review/(?P<name>.*)$', review),
        url(r'^products/$', item_filter),
        url(r'^review_all/(?P<name>.*)$', review_all),
)
