from django.urls import path, include
from rest_framework import routers
from .views import single, customer, indexViewSet

router = routers.DefaultRouter()
router.register(r'customers', indexViewSet)

urlpatterns = [
	path('', include(router.urls)),
	path('customers-auth/', include('rest_framework.urls', namespace = 'rest_framework')),
	path('customer/<int:id>/', single),
	path('new_customer/', customer),

]