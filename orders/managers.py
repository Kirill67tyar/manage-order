"""


1. Реализовать поддержку постраничного вывода списка заказов (объем страницы 10 элементов),
 реализовать сортировку списка заказов по количеству, реализовать фильтрацию списка заказов по марке авто
2. Обеспечить пользовательское представление API в формате OpenApi (Swagger).
3. Реализовать API для получения след. информации:
список цветов с указанием количества заказанных авто каждого цвета (атрибуты элементов: цвет, количество),
список марок с указанием количества заказанных авто каждой марки (атрибуты элементов: марка, количество)

Допущения:
1. Поставщик в состоянии поставить любое количество авто любой марки/модели любого цвета

"""

from django.db.models import Manager, Sum


class OrderManager(Manager):
    def order_by_quantity(self):
        return self.get_queryset().order_by('quantity')

    def filter_by_mark(self, mark):
        return self.get_queryset().filter(model__mark__name=mark)  # .select_related('model__mark')


class ColorManager(Manager):
    def get_queryset(self):
        query = super().get_queryset().annotate(quantity=Sum('orders__quantity'))
        return query


class MarkManager(Manager):
    def get_queryset(self):
        query = super().get_queryset().annotate(quantity=Sum('orders__quantity'))
        return query


class ModelCarManager(Manager):
    def get_queryset(self):
        return super().get_queryset().select_related('mark')
