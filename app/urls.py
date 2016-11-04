from django.conf.urls import include, url
from rest_framework import routers

from app.views import CategoriaViewSet

router = routers.DefaultRouter()
router.register(r'', CategoriaViewSet)

urlpatterns = [
    url(r'categorias/', include(router.urls)),
]
