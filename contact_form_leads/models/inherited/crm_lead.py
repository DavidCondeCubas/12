# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import re
from odoo.exceptions import ValidationError


class CrmLead(models.Model):
    """ Sale Crm Lead model """

    ######################
    # Private Attributes #
    ######################
    _inherit = 'crm.lead'

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
    # preferiría usar un modelo y cargar por defecto las opciones, para que el cliente en algún punto si lo necesitará pueda añadir otras opciones
    source = fields.Selection(
        [('terceros', 'Terceros'), ('redes_sociales', 'Redes Sociales'), ('busqueda', 'Búsqueda en Internet')],
        string="Source")

    def create(self, vals):
        if vals["email_from"]:
            match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$',
                             vals["email_from"])
            if match == None:
                raise ValidationError('Email not valid!')

        return super().create(vals)
