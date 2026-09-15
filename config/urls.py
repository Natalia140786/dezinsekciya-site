from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from services import views
from pages.views import index
from django.urls import include
from pages.views import index, contacts_view, about_view, faq_view
from django.contrib.sitemaps.views import sitemap
from services.sitemap import ServiceSitemap

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('services/', include('services.urls')),
    path('order/', include('orders.urls')),
    path('contacts/', contacts_view, name='contacts'),
    path('about/', about_view, name='about'),
    path('faq/', faq_view, name='faq'),
]

# Добавляем маршруты для медиа-файлов (только в режиме разработки)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

sitemaps = {
    'services': ServiceSitemap,
}

urlpatterns += [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]    

from django.views.generic import TemplateView

urlpatterns += [
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
]

from django.contrib.sitemaps.views import sitemap
from services.sitemap import ServiceSitemap
from pages.sitemap import StaticViewSitemap

sitemaps = {
    'services': ServiceSitemap,
    'static': StaticViewSitemap,
}

urlpatterns += [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
