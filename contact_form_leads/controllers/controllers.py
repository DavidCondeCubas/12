# -*- coding: utf-8 -*-
# from odoo import http


# class ContactFormLeads(http.Controller):
#     @http.route('/contact_form_leads/contact_form_leads/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/contact_form_leads/contact_form_leads/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('contact_form_leads.listing', {
#             'root': '/contact_form_leads/contact_form_leads',
#             'objects': http.request.env['contact_form_leads.contact_form_leads'].search([]),
#         })

#     @http.route('/contact_form_leads/contact_form_leads/objects/<model("contact_form_leads.contact_form_leads"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('contact_form_leads.object', {
#             'object': obj
#         })
