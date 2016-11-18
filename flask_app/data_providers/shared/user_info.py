#!/usr/bin/env python
# -*- coding: utf-8 -*-


class UserInfoDataProvider:
    def __init__(self):
        pass

    def get_data(self, editable):
        return self.sample_data_1(editable)

    def sample_data_0(self, editable):
        data = {
            "editable": editable,
            "current_state": {
                "key": 1,
                "value": "SP",
            },
            "current_city": {
                "key": 1,
                "value": "São José dos Campos",
            },
            "email": "joao@gmail.com",
            "first_name": "João",
            "last_name": "Silva",
            "address": "Rua das esmeraldas - Vila Jurema",
            "address_number": 39,
            "address_complement": "Ed. das Amoeiras, Apt 72",
            "cep": "00000-000",
            "tel": "(12) 98213-6721",
        }
        return data

    def sample_data_1(self, editable):
        data = {
            "editable": editable,
            "state_options": [
                {
                    "key": 1,
                    "value": "SP",
                },
                {
                    "key": 2,
                    "value": "RJ",
                },
                {
                    "key": 3,
                    "value": "MG",
                },
            ],
            "current_state": {
                "key": 1,
                "value": "SP",
            },
            "city_options": [
                {
                    "key": 1,
                    "value": "São José dos Campos",
                },
                {
                    "key": 2,
                    "value": "Jacarei",
                },
            ],
            "current_city": {
                "key": 1,
                "value": "São José dos Campos",
            },
            "email": "joao@gmail.com",
            "first_name": "João",
            "last_name": "Silva",
            "address": "Rua das esmeraldas - Vila Jurema",
            "address_number": 39,
            "address_complement": "Ed. das Amoeiras, Apt 72",
            "state": "SP",
            "city": "São José dos Campos",
            "cep": "00000-000",
            "tel": "(12) 98213-6721",
        }
        return data

user_info_data_provider = UserInfoDataProvider()
