#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import IntEnum, unique

@unique
class OrderStatus(IntEnum):
    PAID = 1
    SHIPPED = 2
    DELIVERED = 3
