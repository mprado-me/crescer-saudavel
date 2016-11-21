#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_app.data_providers.admin.shared.navbar_tab_names import NavbarTabNamesProvider

from flask_app.utils.enums import OrderStatus

from flask import url_for

class NavbarDataProvider:
    def __init__(self):
        pass

    def get_data(self, active_tab_name):
        data = self.sample_data_0()
        self.set_active_tab(data=data, active_tab_name=active_tab_name)
        return data

    def set_active_tab(self, data, active_tab_name):
        for menu_item in data["menu_items"]:
            if menu_item["name"] == active_tab_name:
                menu_item["active"] = True

    def sample_data_0(self):
        data = {
            "menu_items": [
                {
                    "name": NavbarTabNamesProvider.home,
                    "href": url_for("admin_dashboard")
                },
                {
                    "name": NavbarTabNamesProvider.products,
                    "submenu_items": [
                        {
                            "name": "Adicionar novo produto",
                            "href": url_for("admin_add_product"),
                        },
                        {
                            "name": "Visualizar/Editar/Remover produtos",
                            "href": url_for("admin_products", page=1),
                        },
                        {
                            "name": "Adicionar nova categoria",
                            "href": url_for("admin_add_product_category"),
                        },
                        {
                            "name": "Visualizar/Editar/Remover categorias",
                            "href": url_for("admin_product_categories", page=1),
                        },
                        {
                            "name": "Adicionar nova subcategoria",
                            "href": url_for("admin_add_product_subcategory")
                        },
                        {
                            "name": "Visualizar/Editar/Remover subcategorias",
                            "href": url_for("admin_product_subcategories", page=1),
                        },
                    ],
                },
                {
                    "name": NavbarTabNamesProvider.orders,
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
                    "name": NavbarTabNamesProvider.blog,
                    "submenu_items": [
                        {
                            "name": "Adicionar novo post",
                            "href": url_for("admin_add_blog_post"),
                        },
                        {
                            "name": "Visualizar/Editar/Remover posts",
                            "href": url_for("admin_blog_posts", page=1),
                        },
                    ],
                },
                {
                    "name": NavbarTabNamesProvider.customers,
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
                    "name": NavbarTabNamesProvider.images,
                    "submenu_items": [
                        {
                            "name": "Adicionar nova imagem",
                            "href": url_for("admin_add_image"),
                        },
                        {
                            "name": "Visualizar/Remover imagens",
                            "href": url_for("admin_images", page=1),
                        },
                    ],
                },
                {
                    "name": NavbarTabNamesProvider.content,
                    "submenu_items": [
                        {
                            "name": "Home",
                            "href": url_for("admin_content_home"),
                        },
                        {
                            "name": "Contato",
                            "href": url_for("admin_content_contact"),
                        },
                        {
                            "name": "Sobre nós",
                            "href": url_for("admin_content_about_us"),
                        },
                        {
                            "name": "FAQ",
                            "href": url_for("admin_content_faq"),
                        },
                    ],
                },
                {
                    "name": NavbarTabNamesProvider.attended_cities,
                    "submenu_items": [
                        {
                            "name": "Adicionar nova cidade",
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
