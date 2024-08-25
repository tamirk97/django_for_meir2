from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CustomerViewSet, CartViewSet, PurchaseViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'carts', CartViewSet)
router.register(r'purchases', PurchaseViewSet)  

urlpatterns = router.urls
