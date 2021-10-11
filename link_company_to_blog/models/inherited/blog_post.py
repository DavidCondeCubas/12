# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class BlogPost(models.Model):
    """ Blog Post model """

    ######################
    # Private Attributes #
    ######################
    _inherit = 'blog.post'

    ###################
    # Default methods #
    ###################

    ######################
    # Fields declaration #
    ######################
    company_id = fields.Many2one("res.company", related="blog_id.company_id", readonly=1)

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
