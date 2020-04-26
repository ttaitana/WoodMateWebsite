from shop.api.viewsets import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('customer', CustomerViewSet, basename='customer')
router.register('order', OrderViewSet, basename='order')
router.register('product', ProductViewSet, basename='product')
router.register('producttype', ProductTypeViewSet, basename='producttype')
router.register('sales', SalesViewSet, basename='sales')
router.register('orderlist', OrderListViewSet, basename='orderlist')
router.register('cart', CartViewSet, basename='car')
router.register('address', AddressViewSet, basename='address')
router.register('feedback', FeedbackViewSet, basename='feedback')
