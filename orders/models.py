# from django.db import models
from django.db.models import (
    Model, CharField, ForeignKey,
    PositiveIntegerField, DateField, CASCADE,
)

from orders.managers import (
    OrderManager, ColorManager, MarkManager,
)


class ColorCar(Model):
    name = CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name='Цвет'
    )
    objects = ColorManager()

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'


class MarkCar(Model):
    name = CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name='Марка'
    )
    objects = MarkManager()

    class Meta:
        verbose_name = 'Марка'
        verbose_name_plural = 'Марки'


class ModelCar(Model):
    mark = ForeignKey(
        to='MarkCar',
        on_delete=CASCADE,
        related_name='marks',
        verbose_name='id марки'
    )
    name = CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name='Модель'
    )

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'


class OrderCar(Model):
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
    objects = OrderManager()

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

