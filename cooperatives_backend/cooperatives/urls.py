from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CooperativeViewSet

router = DefaultRouter()
# router.register(r'cooperatives', CooperativeViewSet, basename='cooperative')
router.register(r'cooperatives', CooperativeViewSet)



urlpatterns = [
    path('cooperative/', include(router.urls), name='cooperative'),
    path('', include(router.urls), name='api'),
    
]