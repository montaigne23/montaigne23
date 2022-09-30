from odoo import api, fields, models, _

class VillesManagers(models.Model):
    _name = 'open_transport.villes'
    _rec_name = 'name'
    _sql_constraints = [
        ('name_uniq', 'UNIQUE (code)', 'Ce code existe déjà Le code de la ville  doit etre unique')
    ]
    
    code = fields.Char(string='Code Postale', required=True, tracking=True)
    name = fields.Char(string='Ville', required=True, tracking=True)
    pays = fields.Many2one(comodel_name="res.country", string='Pays', required=True, tracking=True)
    region = fields.Char(string='Régions', required=True, tracking=True)