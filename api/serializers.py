from rest_framework import serializers
from api.models import Product, Order, OrderItem

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id', 
            'name', 
            'description', 
            'price', 
            'stock'
        )

        def validate_stock(self, value):
            if value <= 0:
                raise serializers.ValidationError("Stock must be a positive number.")
            return value


class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name')
    product_price = serializers.DecimalField(source='product.price', max_digits=10, decimal_places=2)

    class Meta:
        model = OrderItem
        fields = ('product_name', 'product_price', 'quantity', 'item_subtotal')


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    total_price = serializers.SerializerMethodField()

    def get_total_price(self, obj):
        return sum(item.item_subtotal for item in obj.items.all())

    class Meta:
        model = Order
        fields = (
            'order_id', 
            'user', 
            'status', 
            'created_at',
            'items',
            'total_price'
        )


class ProductInfoSerializer(serializers.Serializer):
    products = ProductSerializer(many=True)
    count = serializers.IntegerField()
    max_price = serializers.FloatField()