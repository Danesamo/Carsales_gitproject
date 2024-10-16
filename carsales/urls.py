from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('greetings.urls')),  # Inclure les URLs de l'application greetings
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
