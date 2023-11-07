from django.contrib import admin
from django.urls import path, include
# from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


api_urls = [
    path('expenses/', include('expenses.urls'))
]

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),


    path('api/portfolio/', include('portfolio.urls')),
    path('api/pet/', include('profiles.urls')),
    path('api/reviews/', include('reviews.urls')),
    path('api/services/', include('services.urls')),
    path('api/visits/', include('visits.urls')),
    path('api/users/', include('users.urls')),

    path('api/v1/', include(api_urls))
]
