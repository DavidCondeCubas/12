# -*- coding: utf-8 -*-
# from odoo import http


# class LinkCompanyToBlog(http.Controller):
#     @http.route('/link_company_to_blog/link_company_to_blog/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/link_company_to_blog/link_company_to_blog/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('link_company_to_blog.listing', {
#             'root': '/link_company_to_blog/link_company_to_blog',
#             'objects': http.request.env['link_company_to_blog.link_company_to_blog'].search([]),
#         })

#     @http.route('/link_company_to_blog/link_company_to_blog/objects/<model("link_company_to_blog.link_company_to_blog"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('link_company_to_blog.object', {
#             'object': obj
#         })
