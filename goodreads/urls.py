from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('books.urls'), name='books'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls'), name='users'),
]
