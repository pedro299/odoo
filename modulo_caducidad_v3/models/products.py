# -*- coding: utf-8 -*-
from odoo import models, fields, api

class products(models.Model):
    _name = 'products'    
    _description = 'Product Lots'
    _creation = 'creation_date desc, name'
    _expiration = 'expiration_date desc, name'
    _notice = 'notice_date desc, name'
    _client = 'customer desc, name'

    name = fields.Char('Product Lots', required = True, index = True)
    description = fields.Html('Description',  sanitize = True, strip_style=False)
    creation = fields.Date('Creation Date', required = True)
    notice = fields.Date('Notice Date', required = True, copy = False)
    expiration = fields.Date('Expiration Date', required = True)

    state = fields.Selection(
        [('new', 'New'),
        ('new to expiry', 'New to expiry'),
        ('timed out', 'Timed out')],
        'Status', default='new', required = True
    )
 
    #Relaciones
    lots_products_ids = fields.Many2many('product.template', string='Products')