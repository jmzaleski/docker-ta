from django.conf.urls import url, include
from rest_framework import routers
from test_tas import views

router = routers.DefaultRouter()

router.register(r'apps', views.AppViewSet)
router.register(r'offers', views.OfferViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
