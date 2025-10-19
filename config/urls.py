from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/v1/courses/', include('apps.courses.urls')),
    path('api/v1/users/', include('apps.users.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
