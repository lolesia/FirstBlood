from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from mami import settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title='Groomimi',
        default_version='v1',
        description='API for Groomimi',
        license=openapi.License(name='IDN'),
    ),
    public=True,
    permission_classes = (permissions.AllowAny,)
)


urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/expenses/', include('expenses.urls')),
    path('api/portfolio/', include('portfolio.urls')),
    path('api/pet/', include('profile.urls')),
    path('api/reviews/', include('reviews.urls')),
    path('api/services/', include('services.urls')),
    path('api/visits/', include('visits.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)