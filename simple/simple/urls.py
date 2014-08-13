from django.conf.urls import patterns, include, url

from main.views import AboutView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', AboutView.as_view(), name='home'),

    url(r'^admin/', include(admin.site.urls)),
)
