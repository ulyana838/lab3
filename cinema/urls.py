from django.contrib import admin  # Импорт модуля admin для настройки административной панели Django
from django.conf import settings  # Импорт настроек Django
from django.conf.urls.static import static  # Импорт функции static для обслуживания статических файлов в режиме разработки
from django.urls import include, path  # Импорт функций include и path для определения маршрутов URL

urlpatterns = [  # Определение списка URL-маршрутов для проекта
    path('admin/', admin.site.urls),  # Определение маршрута для административной панели Django
    path('', include('app.urls')),  # Определение маршрута для включения URL-маршрутов из приложения 'app'
] 
