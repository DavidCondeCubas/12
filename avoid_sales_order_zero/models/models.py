# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class avoid_sales_order_zero(models.Model):
#     _name = 'avoid_sales_order_zero.avoid_sales_order_zero'
#     _description = 'avoid_sales_order_zero.avoid_sales_order_zero'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
