from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from .chat import urls as chat_urls
from .kanban import urls as kanban_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include(chat_urls)),
    path('kanban/', include(kanban_urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
