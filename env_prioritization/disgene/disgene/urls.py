"""disgene URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from diseasemods import views as diseasemods_views
from contact.views import  ContactView, contact, ContactFormView
from ontomap.views import  OntologyMapView
from nanopub import views as nanopub_views
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^$', diseasemods_views.home, name='home'),
    url(r'^contact/', contact, name='contact'),
    url(r'^contact-cbv/', ContactView.as_view(), name='contact_cbv'),
    url(r'^ontomap/$', TemplateView.as_view(template_name='ontomap.html'), name='ontomap'),
    url(r'^ontomap-list/$', OntologyMapView.as_view(), name='ontomap_list'),
    url(r'^nanopub/', TemplateView.as_view(template_name='contact.html'), name='nanopub'),
    url(r'^contact-form/$', ContactFormView.as_view(), name='contact_form'),
    url(r'^tools/literature$',  TemplateView.as_view(template_name="contact.html"), name='literature'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
