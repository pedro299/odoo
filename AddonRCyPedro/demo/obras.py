from odoo import models, fields


class obras(models.Model):
    _name = "obras"
    _description = "Listado de obras pertenecientes a los artistas"

    name = fields.Char('Title', required=True, index=True)
    description = fields.Html('Description', required=True)
    obra_id = fields.Integer(required=True, index=True)
    style = fields.Text('Style used', required=True)
    date_start = fields.Date('Date started')
    date_end = fields.Date('Date finished')

    artistas = fields.Many2many('artistas', string='Artistas')

    state = fields.Selection(
        [('unfinished', 'unfinished'),
         ('finished', 'finished'),
         ('a_medias', 'a_medias')],
        'State', default="unfinished", required=True
    )