from odoo import api, fields, models, _

class AssuranceManagers(models.Model):
    _name = 'open_transport.assurance'
    
    cout = fields.Float(string="Valeur d'assurance", required=True, tracking=True)
    poids = fields.Integer(string='Poids du camion', required=True, tracking=True)
    type_cam = fields.Many2one(string="Model de camion", required=True, tracking=True, comodel_name='fleet.vehicle.model')
    