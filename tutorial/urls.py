from django.conf.urls import url, include
from django.contrib import admin
from tutorial import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.handlers import StaticFilesHandler
from django.core.wsgi import get_wsgi_application

urlpatterns = [
    url(r'^$', views.login_redirect, name='login_redirect'),
    url(r'^admin/', admin.site.urls),
    url(r'^account/', include('accounts.urls', namespace = 'accounts')),
    url(r'^home/', include('home.urls', namespace = 'home')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns



