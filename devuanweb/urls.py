from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

#from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='index.html'), {'name': 'homepage'}, name='homepage'),
    url(r'^donate$', TemplateView.as_view(template_name='donate.html'), {'name': 'donate'}, name='donate'),

    #url(r'^admin/', include(admin.site.urls)),
)
