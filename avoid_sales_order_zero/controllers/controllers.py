# -*- coding: utf-8 -*-
# from odoo import http


# class AvoidSalesOrderZero(http.Controller):
#     @http.route('/avoid_sales_order_zero/avoid_sales_order_zero/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/avoid_sales_order_zero/avoid_sales_order_zero/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('avoid_sales_order_zero.listing', {
#             'root': '/avoid_sales_order_zero/avoid_sales_order_zero',
#             'objects': http.request.env['avoid_sales_order_zero.avoid_sales_order_zero'].search([]),
#         })

#     @http.route('/avoid_sales_order_zero/avoid_sales_order_zero/objects/<model("avoid_sales_order_zero.avoid_sales_order_zero"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('avoid_sales_order_zero.object', {
#             'object': obj
#         })
