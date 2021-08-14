from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework_jwt.views import obtain_jwt_token

from rest_framework import routers

from short_url.views import UrlsViewSet

router = routers.DefaultRouter()
router.register('/m2b', UrlsViewSet, basename='Urls')

urlpatterns = [
    path('api', include(router.urls)),
    path('m2b/', include('short_url.urls')),
    path('admin/', admin.site.urls),
    path('login/', obtain_jwt_token, name='login-jwt'),
]

handler400 = 'short_url.views.error_500_view'
handler404 = 'short_url.views.error_404_view'
handler500 = 'short_url.views.error_500_view'
