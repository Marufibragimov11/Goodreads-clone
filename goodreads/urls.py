from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from .views import landing_page

urlpatterns = [
    path("", landing_page, name="landing_page"),
    path("users/", include("users.urls")),
    path("books/", include("books.urls")),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
