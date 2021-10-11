from odoo import api, SUPERUSER_ID


def add_source_to_whitelist(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    env['ir.model.fields'].formbuilder_whitelist('crm.lead', ['source'])
