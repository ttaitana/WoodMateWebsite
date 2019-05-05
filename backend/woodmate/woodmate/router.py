from shop.api.viewsets import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('customer', CustomerViewSet, base_name='customer')
router.register('order', OrderViewSet, base_name='order')
router.register('product', ProductViewSet, base_name='product')
router.register('producttype', ProductTypeViewSet, base_name='producttype')
router.register('sales', SalesViewSet, base_name='sales')
router.register('orderlist', OrderListViewSet, base_name='orderlist')
router.register('cart', CartViewSet, base_name='car')
router.register('address', AddressViewSet, base_name='address')
router.register('feedback', FeedbackViewSet, base_name='feedback')
