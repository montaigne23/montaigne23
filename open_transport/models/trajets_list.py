from odoo import api, fields, models, _


class TrajetsList(models.Model):
    _inherits = {'open_transport.gestiontrajets': 'trajet_id'}
    _name = 'open_transport.trajets_list_custom'
    # _rec_name = 'code'
    
    trajet_id = fields.Many2one( string="Trajets choice",
        comodel_name='open_transport.gestiontrajets', required=True, ondelete='cascade',
        delegate=True,)
    dossier_id = fields.Many2one( string="Dossier",
        comodel_name='open_transport.dossier', invisible=True)
    nbr_colis = fields.Float(required=True, tracking=True)
    designation = fields.Char(string="Designation", required=True)
    poids_brute = fields.Float(required=True, tracking=True)
    Cubage = fields.Char(tracking=True)
    # depard = fields.Char(string="depard", compute="depard_compute")
    # arrive = fields.Char(string="arrive", compute="arrive_compute")
    # cout = fields.Float(string="Coût", compute="amende_compute")
    
                
    # @api.onchange('trajet_id')
    # def depard_compute(self):
    #     self.depard = self.trajet_id.depard.name
        
        
    # @api.onchange('trajet_id')
    # def arrive_compute(self):
    #     self.arrive = self.trajet_id.arrive.name
        
    # @api.onchange('trajet_id')
    # def amende_compute(self):
    #     self.cout = self.trajet_id.amende
        