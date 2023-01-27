from django.contrib.admin import site
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt

    
urlpatterns = [
    path('', include('pages.urls')),
    path('listings/', include('listings.urls')),
    path('contacts/', include('contacts.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', csrf_exempt(site.urls)),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
