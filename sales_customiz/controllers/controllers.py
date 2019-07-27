# -*- coding: utf-8 -*-
from openerp import http

# class SalesCustomiz(http.Controller):
#     @http.route('/sales_customiz/sales_customiz/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sales_customiz/sales_customiz/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sales_customiz.listing', {
#             'root': '/sales_customiz/sales_customiz',
#             'objects': http.request.env['sales_customiz.sales_customiz'].search([]),
#         })

#     @http.route('/sales_customiz/sales_customiz/objects/<model("sales_customiz.sales_customiz"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sales_customiz.object', {
#             'object': obj
#         })