# from django.db import models
from django.db.models import (
    Model, CharField, ForeignKey,
    PositiveIntegerField, DateField, CASCADE,
)

from orders.managers import (
    OrderManager, ColorManager,
    MarkManager, ModelCarManager
)


class ColorCar(Model):
    name = CharField(
        max_length=50,
        null=False,
        blank=False,
        unique=True,
        verbose_name='Цвет'
    )
    # objects = ColorManager()

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'

    def __str__(self):
        return f'{self.name}'


class MarkCar(Model):
    name = CharField(
        max_length=50,
        null=False,
        blank=False,
        unique=True,
        verbose_name='Марка'
    )
    # objects = MarkManager()

    class Meta:
        verbose_name = 'Марка'
        verbose_name_plural = 'Марки'

    def __str__(self):
        return f'{self.name}'


class ModelCar(Model):
    mark = ForeignKey(
        to='MarkCar',
        on_delete=CASCADE,
        related_name='models',
        verbose_name='id марки'
    )
    name = CharField(
        max_length=50,
        null=False,
        blank=False,
        unique=True,
        verbose_name='Модель'
    )
    # objects = ModelCarManager()

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'

    def __str__(self):
        return f'{self.mark.name} {self.name}'


class Order(Model):
    color = ForeignKey(
        to='ColorCar',
        on_delete=CASCADE,
        related_name='orders',
        verbose_name='id цвета'
    )
    model = ForeignKey(
        to='ModelCar',
        on_delete=CASCADE,
        related_name='orders',
        verbose_name='id модели'
    )
    quantity = PositiveIntegerField(
        null=False,
        blank=False,
        verbose_name='Количество'
    )
    timestamp = DateField(
        auto_now_add=True,
        verbose_name='Время создания заказа'
    )
    # objects = OrderManager()

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    # def __str__(self):
    #     return f'{self.model.mark.name} {self.model.name} ({self.color.name}) - {self.quantity} шт.'

    def __str__(self):
        return f'Заказ № {self.pk}'
