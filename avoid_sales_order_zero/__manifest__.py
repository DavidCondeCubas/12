# -*- coding: utf-8 -*-
{
    'name': "avoid_sales_order_zero",

    'summary': """
        NO PERMITIR PEDIDOS DE VENTA CON CANTIDADES CERO""",

    'description': """
        Se trata de impedir pedidos de venta con cantidad de productos a cero. Si el usuario pulsa el botón
de confirmación de venta con cantidades de productos a cero, se mostrará una advertencia y se impedirá
la continuación del flujo de venta.
Como complementación, se pide añadir un botón en la cabecera del pedido de venta que borre
precisamente sólo aquellas líneas que tengan la cantidad del producto a cero.
    """,

    'author': "David Conde Cubas",
    'website': "https://www.linkedin.com/in/david-conde-cubas-6a16a619a",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
