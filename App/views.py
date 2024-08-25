from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Product, Customer, Cart, Purchase
from .serializers import ProductSerializer, CustomerSerializer, CartSerializer, PurchaseSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def checkout(self, request, pk=None):
        cart = self.get_object()
        if not cart.is_checked_out:
            for product in cart.products.all():
                Purchase.objects.create(
                    customer=cart.customer,
                    product=product,
                    cart=cart,
                    quantity=1,  # Adjust quantity logic as needed
                    total_price=product.price
                )
            cart.is_checked_out = True
            cart.products.clear()
            cart.save()
            return Response({'message': 'Checkout successful'}, status=status.HTTP_200_OK)
        return Response({'message': 'Cart already checked out'}, status=status.HTTP_400_BAD_REQUEST)

class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = [IsAuthenticated]
