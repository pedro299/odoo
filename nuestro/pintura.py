from odoo import models, fields


class pintura(models.Model):
    _name = 'pinturas'
    _description = 'Pinturas'

    name = fields.Char('Nombre', required=True, index=True)
    '''Id pintura tiene que heredar de la id de la pintura'''
    #id_pintura = ()

    color = fields.Char('Color', required=True)
    id_color = fields.Integer('Id color', required=True, index=True)
    paint_type = fields.Selection(
        [('Mate', 'Mate'),
         ('Óleo', 'Óleo'),
         ('Acrílica', 'Acrílica'),
         ('Metalizada', 'Metalizada'),
         ('Temple', 'Temple')],
        'Type', default="Mate", required=True
    )
