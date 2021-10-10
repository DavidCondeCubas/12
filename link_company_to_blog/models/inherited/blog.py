# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class Blog(models.Model):
    """ Student model """

    ######################
    # Private Attributes #
    ######################
    _inherit = 'blog.blog'

    ###################
    # Default methods #
    ###################

    ######################
    # Fields declaration #
    ######################
    company_id = fields.Many2one("res.company")

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