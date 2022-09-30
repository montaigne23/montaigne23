from odoo import api, fields, models, _

class ResPartner(models.Model):
    _name = 'open_transport.res_partner'
    _rec_name = "partner_id"
    partner_id = fields.Many2one(comodel_name="res.partner", String="Le Fournisseur", required=True)
    dossier_id = fields.Many2one(comodel_name="open_transport.dossier", String="Dossier", invisible=True)
    marque_vehicule = fields.Char(String="Marque du vehicule", required=True)
    numero_vehicule = fields.Char(String="Numero du vehicule", required=True)
    Nbr_colis = fields.Char(String="Numbre de Colis", required=True)
    trajet_id = fields.Many2one(comodel_name="open_transport.gestiontrajets", String="Trajet", required=True)
    poids_brute = fields.Float(String="Poids Brut")
    Cubage = fields.Char(String="Cubage")
    Cout = fields.Float(String="Coût", required=True)
    