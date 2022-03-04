# -*- coding: utf-8 -*-
# from odoo import http


# class ModuloCaducidad(http.Controller):
#     @http.route('/modulo_caducidad/modulo_caducidad/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_caducidad/modulo_caducidad/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_caducidad.listing', {
#             'root': '/modulo_caducidad/modulo_caducidad',
#             'objects': http.request.env['modulo_caducidad.modulo_caducidad'].search([]),
#         })

#     @http.route('/modulo_caducidad/modulo_caducidad/objects/<model("modulo_caducidad.modulo_caducidad"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_caducidad.object', {
#             'object': obj
#         })
