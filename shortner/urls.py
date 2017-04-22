from django.conf.urls import url
from .views import *

urlpatterns = [

    url(r'^$', home, name='home'),
    # for our home/index page

    url(r'^(?P<slug>[-\w]+)/$', redirect_original, name='original'),

# url(r'^(?P&lt;short_id&gt;\w{6})$', 'redirect_original', name='redirectoriginal'),
    # when short URL is requested it redirects to original URL

  #  url(r'^makeshort/$', 'shorten_url', name='shortenurl'),
]
