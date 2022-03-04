# -*- coding: utf-8 -*-
from odoo import models, fields


class artistas(models.Model):
    _name = 'artistas'
    _description = 'descripcion desc, desc'
    _apodo = 'apodo desc, name'

    name = fields.Char('Nombre', required=True, index=True)
    apellidos = fields.Char('Apellidos', required=True)
    apodo = fields.Char('Apodo')
    descripcion = fields.Text('Descripcion del artista')
    id_artista = fields.Integer('Id artista', required=True, index=True)
    tipo = fields.Selection(
        [('artista', 'artista'), ('pintor_de_construccion', 'pintor_de_construccion'),
         ('restaurador', 'restaurador'), ('ayudante', 'ayudante')]
    )
    nacimiento = fields.Date('Fecha de nacimiento')

    direccion = fields.Many2one('direccion', string='Direccion')
    obras = fields.Many2many('obras', string='Obras del artista')
