from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from mami import settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from users.social_views import GoogleLogin, FacebookLogin



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

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('accounts/', include('allauth.urls')),  # Allauth
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    # path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('accounts/social/', include('allauth.socialaccount.urls')),
    path('accounts/social/login/google/', GoogleLogin.as_view()),
    path('accounts/social/login/facebook/', FacebookLogin.as_view(), name='fb_login'),



    path('api/expenses/', include('expenses.urls')),
    path('api/portfolio/', include('portfolio.urls')),
    path('api/pet/', include('profile.urls')),
    path('api/reviews/', include('reviews.urls')),
    path('api/services/', include('services.urls')),
    path('api/visits/', include('visits.urls')),
    path('api/users/', include('users.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
