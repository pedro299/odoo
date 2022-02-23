# -*- coding: utf-8 -*-
from datetime import timedelta
 
from odoo import models, fields, api
from odoo.exceptions import ValidationError
 
class lot(models.Model):
    _name = 'lot'
    _description = 'Product Lots'
    _creation = 'creation_date desc, name'
    _expiration = 'expiration_date desc, name'
    _notice = 'notice_date desc, name'
    _client = 'customer desc, name'
 
    name = fields.Char('Product Lots', required = True, index = True)
    description = fields.Html('Description', sanitize = True, strip_style=False)
    creation = fields.Date('Creation Date', required = True)
    expiration = fields.Date('Expiration Date', required = True)

    state = fields.Selection(
        [('New', 'New'),
        ('New to expiry', 'New to expiry'),
        ('Timed out', 'Timed out')],
        'Status', default='New', required = True
    )

    notice = fields.Datetime('Notice Date', required = True, copy = False)
 
    #Relaciones
    lots_products = fields.Many2many('product.template', string='Products')
