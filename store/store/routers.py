from rest_framework.routers import DefaultRouter
from category.api import ProductViewSet

router = DefaultRouter()

router.register(r'products', ProductViewSet, base_name='product')


