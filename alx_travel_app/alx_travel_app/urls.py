# project urls
from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# swagger setup
schema_view = get_schema_view(
    openapi.Info(
        title="ALX Travel API",
        default_version='v1',
        description="API documentation",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listings/', include('listings.urls')),     
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0)),
]
