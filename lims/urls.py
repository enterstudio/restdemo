from django.conf.urls import url, include
from rest_framework import routers
from samples import views

router = routers.DefaultRouter()
router.register(r'samples', views.SampleViewSet)
router.register(r'assays', views.AssayViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
