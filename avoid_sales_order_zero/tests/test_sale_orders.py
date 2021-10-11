from dateutil.relativedelta import relativedelta
from datetime import datetime
from odoo.exceptions import UserError, AccessError
from odoo.tests import common


class TestSaleOrders(common.TransactionCase):
    def test_confirm_with_zero_qty(self):
        test_customer_id = self.env['res.partner'].create({'name': 'test_cust'})
        test_product_id = self.env['product.template'].create({'name': 'test_product'})
        record = self.env['sale.order'].create({
            'partner_id': test_customer_id.id,
            'order_line': [(0, 0, {'product_id': test_product_id.id, 'product_uom_qty': 0}),
                           (0, 0, {'product_id': test_product_id.id, 'product_uom_qty': 10})]
        })
        self.assertRaises(record.action_confirm())

    def test_remove_order_lines(self):
        test_customer_id = self.env['res.partner'].create({'name': 'test_cust'})
        test_product_id = self.env['product.template'].create({'name': 'test_product'})
        record = self.env['sale.order'].create({
            'partner_id': test_customer_id.id,
            'order_line': [(0, 0, {'product_id': test_product_id.id, 'product_uom_qty': 0}),
                           (0, 0, {'product_id': test_product_id.id, 'product_uom_qty': 10})]
        })
        record.remove_order_line_zero_units()
        self.assertTrue(
            len(record.order_line) == 1 and len(record.order_line.filtered(lambda x: x.product_uom_qty)) == 1)
