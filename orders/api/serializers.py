from django.db.models import Sum
from rest_framework.serializers import (
    SerializerMethodField,
    ModelSerializer,
    Serializer,
)

from orders.models import (
    Order, ColorCar, MarkCar, ModelCar,
)


class ColorCarSerializer(ModelSerializer):
    quantity_in_orders = SerializerMethodField(read_only=True)
    qs = ColorCar.objects.all().annotate(quantity=Sum('orders__quantity')).values('id', 'quantity')

    def get_quantity_in_orders(self, obj):  # obj - экземпляр Note
        for m in self.qs:
            if m['id'] == obj.pk:
                return m['quantity']

    class Meta:
        model = ColorCar
        fields = ('id', 'name', 'quantity_in_orders',)
        extra_kwargs = {
            'id': {'read_only': True, }
        }


class MarkCarSerializer(ModelSerializer):
    quantity_in_orders = SerializerMethodField(read_only=True)
    qs = MarkCar.objects.all().annotate(quantity=Sum('models__orders__quantity')).values('id', 'quantity')

    def get_quantity_in_orders(self, obj):  # obj - экземпляр Note
        for m in self.qs:
            if m['id'] == obj.pk:
                return m['quantity']

    class Meta:
        model = MarkCar
        fields = ('id', 'name', 'quantity_in_orders',)
        extra_kwargs = {
            'id': {'read_only': True, }
        }


class ModelCarSerializer(ModelSerializer):
    mark = MarkCarSerializer(many=False, read_only=False)

    class Meta:
        model = ModelCar
        fields = ('id', 'name', 'mark',)
        extra_kwargs = {
            'id': {'read_only': True, }
        }


class OrderSerializer(ModelSerializer):
    model = ModelCarSerializer(many=False, read_only=False)
    color = ColorCarSerializer(many=False, read_only=False)

    class Meta:
        model = Order
        fields = ('id', 'color', 'model', 'quantity', 'timestamp',)
        extra_kwargs = {
            'id': {'read_only': True, }
        }


"""
    color = ForeignKey to ColorCar
    model = ForeignKey to ModelCar
    quantity = PositiveIntegerField
    timestamp = DateField

class ColorCar(Model):
    name = CharField
    
class MarkCar(Model):
    name = CharField

class ModelCar(Model):
    mark = ForeignKey to MarkCar
    name = CharField


class Order(Model):
    color = ForeignKey to ColorCar
    model = ForeignKey to ModelCar
    quantity = PositiveIntegerField
    timestamp = DateField


"""
