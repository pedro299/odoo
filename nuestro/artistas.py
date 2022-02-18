# -*- coding: utf-8 -*-
from odoo import models, fields


class artistas(models.Model):
    _name = 'artistas'
    _description = 'Artista'

    name = fields.Char('Nombre', required=True, index=True)
    apellidos = fields.Char('Apellidos', required=True)
    apodo = fields.Char('Apodo')
    descripcion = fields.Text('Descripcion del artista')
    id_artista = fields.Integer('Id artista', required=True, index=True)
    tipo = fields.Selection(
        [('Artista'), ('Pintor de Construccion'), ('Restaurador'), ('Ayudante')]
    )
    nacimiento = fields.Date('Fecha de nacimiento')

    direccion = fields.One2many('direccion', string='Direccion')
    obras = fields.Many2many('obras', string='Obras del artista')
