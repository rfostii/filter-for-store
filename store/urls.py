from django.conf import settings
from django.conf.urls.defaults import *
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import settings


urlpatterns = staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
from django.contrib import admin
admin.autodiscover()
urlpatterns += patterns('',
                        url(r'^store/', include('apps.urls')),
                        (r'^static/(?P<path>.*)$', 'django.views.static.serve',
                         {'document_root':settings.STATIC_ROOT }),
                        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                         {'document_root':settings.MEDIA_ROOT }),
                        url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                        url(r'^admin/', include(admin.site.urls)),
)


