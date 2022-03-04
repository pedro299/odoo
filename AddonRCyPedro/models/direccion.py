# -*- coding: utf-8 -*-
from odoo import models, fields


class direccion(models.Model):
    _name = 'direccion'
    _description = 'Direccion de obra o artista'

    name = fields.Char('Direccion', required=True, index=True)
    ciudad = fields.Char('Ciudad', index=True)
    provincia = fields.Char('Provincia', index=True)
    pais = fields.Char('Pais', index=True)
    tipo = fields.Selection(
        [('calle', 'calle'), ('avenida', 'avenida'), ('bulevar', 'bulevar'),
         ('plaza', 'plaza'), ('travesia', 'travesia'), ('urbanizacion', 'urbanizacion')]
    )
    numero = fields.Integer('Numero', required=True)
    piso = fields.Integer('Piso')
    letra = fields.Char('Letra')
    # artistas = One2many('artistas', string = 'artistas')
