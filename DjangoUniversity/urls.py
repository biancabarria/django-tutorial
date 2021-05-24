from django.contrib import admin
from django.urls import include, path

urlpatterns = [
 path('DjangoUniApp/', include('DjangoUniApp.urls')),
 path('admin/', admin.site.urls),
]
