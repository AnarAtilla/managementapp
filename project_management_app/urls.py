from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from projects_m import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # Аутентификация через django-allauth
    path('api/', include('projects_m.urls')),  # API маршруты
    path('', views.home, name='home'),  # Добавьте эту строку
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
