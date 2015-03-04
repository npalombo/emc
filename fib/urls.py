from django.conf.urls import patterns, include, url

from webapp import api

urlpatterns = patterns('',
    url(r'^fib/(-?\w+)', api.fib_api),
)
