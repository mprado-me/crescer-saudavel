#!/usr/bin/env python
# -*- coding: utf-8 -*-

class TotalTableDataProvider():
    def get_fresh_order_data(self, user_email):
        return self.get_sample_data_0()

    def get_sample_data_0(self):
        return {
            "products_total": "R$ 32,60",
            "frete": "R$ 5,00",
            "total": "R$ 37,60",
        }

    def get_old_order_data(self, order_id):
        return self.get_sample_data_1()

    def get_sample_data_1(self):
        return {
            "products_total": "R$ 32,60",
            "frete": "R$ 5,00",
            "total": "R$ 37,60",
        }