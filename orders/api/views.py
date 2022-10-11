from rest_framework.viewsets import ModelViewSet
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_405_METHOD_NOT_ALLOWED,

)

from orders.api.utils import (
    HTTP_METHOD_NAMES,
    ResultsSetPagination,
)
from orders.api.serializers import (
    ColorCarSerializer, MarkCarSerializer,
    ModelCarSerializer, OrderSerializer,
)
from orders.models import (
    ColorCar, MarkCar, ModelCar, Order,
)


class ColorCarModelViewSet(ModelViewSet):
    serializer_class = ColorCarSerializer
    queryset = ColorCar.objects.all()
    http_method_names = HTTP_METHOD_NAMES


class MarkCarModelViewSet(ModelViewSet):
    serializer_class = MarkCarSerializer
    queryset = MarkCar.objects.all()
    http_method_names = HTTP_METHOD_NAMES


class ModelCarModelViewSet(ModelViewSet):
    serializer_class = ModelCarSerializer
    queryset = ModelCar.objects.all()
    http_method_names = HTTP_METHOD_NAMES


class OrderModelViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all().select_related('model__mark', 'color')
    http_method_names = HTTP_METHOD_NAMES
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        mark = self.request.query_params.get('mark')
        order_by_quantity = self.request.query_params.get('order_by_quantity')
        if mark:
            self.queryset = self.queryset.filter(model__mark__name=mark)
        if order_by_quantity:
            self.queryset = self.queryset.order_by('quantity')
        return super().get_queryset()


"""
список марок с указанием количества заказанных авто каждой марки (атрибуты элементов: марка, количество)
MarkCar.objects.all().annotate(quantity=Sum('models__orders__quantity'))


Order.objects.all().order_by('quantity')

Order.objects.filter(model__mark__name=mark)  # .select_related('model__mark')
"""
