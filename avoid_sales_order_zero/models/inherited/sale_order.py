# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    """ Sale Order model """

    ######################
    # Private Attributes #
    ######################
    _inherit = 'sale.order'

    ###################
    # Default methods #
    ###################

    ######################
    # Fields declaration #
    ######################

    ##############################
    # Compute and search methods #
    ##############################

    ############################
    # Constrains and onchanges #
    ############################

    #########################
    # CRUD method overrides #
    #########################

    ##################
    # Action methods #
    ##################

    ####################
    # Business methods #
    ####################
    def action_confirm(self):
        order_lines_with_zero_units = self.order_line.filtered(lambda x: int(x.product_uom_qty) == 0).mapped(
            lambda y: 'El producto %s debe tener mas de 0 unidades seleccionadas.' % y.product_id.name)

        if order_lines_with_zero_units:
            raise ValidationError('\n'.join(order_lines_with_zero_units))

        return super(SaleOrder, self).action_confirm()

    def remove_order_line_zero_units(self):
        order_lines_with_zero_units = self.order_line.filtered(lambda x: int(x.product_uom_qty) == 0)
        if order_lines_with_zero_units:
            order_lines_with_zero_units.unlink()
