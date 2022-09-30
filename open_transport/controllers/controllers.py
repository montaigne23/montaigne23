# -*- coding: utf-8 -*-
# from odoo import http


# class OpenTransport(http.Controller):
#     @http.route('/open_transport/open_transport', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/open_transport/open_transport/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('open_transport.listing', {
#             'root': '/open_transport/open_transport',
#             'objects': http.request.env['open_transport.open_transport'].search([]),
#         })

#     @http.route('/open_transport/open_transport/objects/<model("open_transport.open_transport"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('open_transport.object', {
#             'object': obj
#         })
