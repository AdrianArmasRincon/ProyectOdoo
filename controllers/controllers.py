# -*- coding: utf-8 -*-
# from odoo import http


# class Proyectoadrianarmas(http.Controller):
#     @http.route('/proyectoadrianarmas/proyectoadrianarmas', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/proyectoadrianarmas/proyectoadrianarmas/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('proyectoadrianarmas.listing', {
#             'root': '/proyectoadrianarmas/proyectoadrianarmas',
#             'objects': http.request.env['proyectoadrianarmas.proyectoadrianarmas'].search([]),
#         })

#     @http.route('/proyectoadrianarmas/proyectoadrianarmas/objects/<model("proyectoadrianarmas.proyectoadrianarmas"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('proyectoadrianarmas.object', {
#             'object': obj
#         })
