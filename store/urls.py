from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('online_store.urls')),
    path('cart/', include('cart.urls')),
    path('administration/', include('application.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
