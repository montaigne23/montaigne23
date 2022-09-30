# -*- coding: utf-8 -*-
# from odoo import http


# class PostCloture(http.Controller):
#     @http.route('/post_cloture/post_cloture', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/post_cloture/post_cloture/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('post_cloture.listing', {
#             'root': '/post_cloture/post_cloture',
#             'objects': http.request.env['post_cloture.post_cloture'].search([]),
#         })

#     @http.route('/post_cloture/post_cloture/objects/<model("post_cloture.post_cloture"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('post_cloture.object', {
#             'object': obj
#         })
