from django.contrib.admin import ModelAdmin, register

from orders.models import (
    Order, ColorCar, ModelCar, MarkCar,
)


@register(Order)
class OrderAdmin(ModelAdmin):
    fields = ('color', 'model', 'quantity',)


@register(ColorCar)
class ColorCarAdmin(ModelAdmin):
    fields = ('name',)


@register(ModelCar)
class ModelCarAdmin(ModelAdmin):
    fields = ('name', 'mark',)


@register(MarkCar)
class MarkCarAdmin(ModelAdmin):
    fields = ('name',)
