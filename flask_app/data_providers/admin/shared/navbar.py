#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_app.utils.enums import OrderStatus

from flask import url_for

class NavbarDataProvider:
    def __init__(self):
        pass

    def get_data(self):
        return self.sample_data_0()

    def sample_data_0(self):
        data = {
            "menu_items": [
                {
                    "name": "Home",
                    "active": True,
                    "href": url_for("admin_dashboard")
                },
                {
                    "name": "Produtos",
                    "submenu_items": [
                        {
                            "name": "Adicionar produto",
                            "href": url_for("admin_add_product"),
                        },
                        {
                            "name": "Visualizar/Editar/Remover produtos",
                            "href": url_for("admin_products", page=1),
                        },
                    ],
                },
                {
                    "name": "Pedidos",
                    "submenu_items": [
                        {
                            "name": "Pagos",
                            "href": url_for("admin_orders", order_status=int(OrderStatus.PAID), page=1),
                        },
                        {
                            "name": "Enviados",
                            "href": url_for("admin_orders", order_status=int(OrderStatus.SHIPPED), page=1),
                        },
                        {
                            "name": "Entregues",
                            "href": url_for("admin_orders", order_status=int(OrderStatus.DELIVERED), page=1),
                        },
                    ],
                },
                {
                    "name": "Blog",
                    "submenu_items": [
                        {
                            "name": "Adicionar post",
                            "href": url_for("admin_add_blog_post"),
                        },
                        {
                            "name": "Visualizar/Editar/Remover posts",
                            "href": url_for("admin_blog_posts", page=1),
                        },
                    ],
                },
                {
                    "name": "Clientes",
                    "submenu_items": [
                        {
                            "name": "Cadastrados",
                            "href": url_for("admin_registered_customers", page=1),
                        },
                        {
                            "name": "Newsletter",
                            "href": url_for("admin_newsletter_customers", page=1),
                        },
                    ],
                },
                {
                    "name": "Imagens",
                    "submenu_items": [
                        {
                            "name": "Adicionar imagem",
                            "href": url_for("admin_add_image"),
                        },
                        {
                            "name": "Visualizar/Remover imagens",
                            "href": url_for("admin_images", page=1),
                        },
                    ],
                },
                {
                    "name": "Conteúdo",
                    "submenu_items": [
                        {
                            "name": "Home",
                            "href": url_for("admin_content_home"),
                        },
                    ],
                },
                {
                    "name": "Cidades atendidas",
                    "submenu_items": [
                        {
                            "name": "Adicionar cidade",
                            "href": url_for("admin_add_attended_city"),
                        },
                        {
                            "name": "Visualizar/Remover cidades",
                            "href": url_for("admin_attended_cities", page=1),
                        },
                    ],
                },
            ]
        }
        return data

navbar_data_provider = NavbarDataProvider()
