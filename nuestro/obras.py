from odoo import models, fields


class obras(models.Model):
    _name = "obras"
    _description = "Listado de obras pertenecientes a los artistas"

    name = fields.Char('Title', required=True, index=True)
    description = fields.Html('Description', required=True)
    obra_id = fields.Integer(required=True, index=True)
    style = fields.Text('Style used' required=True)
    date_start = fields.Date('Date started', required=false)
    date_end = fields.Date('Date finished', copy=false)

    author_id = fields.Many2many('artistas')
    pintura = fields.One2many('direccion')

    paint_type = fields.Selection(
        [('Mate'), ('Óleo'), ('Acrílica'),
         ('Metalizada'), ('Temple')],
        'Type', default="Mate"
    )
    state = fields.Selection(
        [('unfinished', 'Unfinished'),
         ('finished', 'Finished'),
         ('a medias', 'A medias')],
        'State', default="unfinished"
    )
