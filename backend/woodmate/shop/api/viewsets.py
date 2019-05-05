from shop.models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

# class CustomerViewSet(viewsets.ViewSet):
#     def list(self, request):
#         queryset = Customer.objects.all()
#         serializer = CustomerSerializer(queryset, many=True)
#         return Response(serializer.data)

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer

class SalesViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer

class DeliveryManViewSet(viewsets.ModelViewSet):
    queryset = DeliveryMan.objects.all()
    serializer_class = DeliveryManSerializer

class OrderListViewSet(viewsets.ModelViewSet):
    queryset = OrderList.objects.all()
    serializer_class = OrderListSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
