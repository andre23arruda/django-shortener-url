from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import *

urlpatterns = [
    path('<short_url>', redirect_url, name='redirect_url'),
]