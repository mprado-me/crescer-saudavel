#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import IntEnum, unique

@unique
class OrderStatus(IntEnum):
    PAID = 1
    SHIPPED = 2
    DELIVERED = 3


@unique
class ProductSortMethod(IntEnum):
    NAME = 1
    LOWEST_PRICE = 2
    BIGGEST_PRICE = 3
    BEST_SELLER = 4


@unique
class AdminProductsSortMethod(IntEnum):
    TITLE = 1
    LOWEST_PRICE = 2
    BIGGEST_PRICE = 3
    LOWEST_STOCK = 4
    HIGHER_STOCK = 5
    BEST_SELLER = 6
    LESS_SOLD = 7
