
from odoo import models, fields, api


class post_cloture_sexion_line(models.Model):
    
    # _inherits = {'res.user':'user_id'}
    _name = 'post_cloture.sexion_line'
    _description = 'post_cloture.sexion_line'

    user_id = fields.Many2one(string="Caissier",
                              comodel_name='res.users',
                               required=True)
    
    sexion_id = fields.Many2one(string="Sexion",
                             comodel_name='post_cloture.sexion',
                             required=False 
                              )
    
    date_start = fields.Datetime(string="Date d'ouverture", required=True)
    date_close = fields.Datetime(string="Date de fermeture", required=True)

    total_sale = fields.Float(string="Total de Vente", compute="total_vente")
    total_liquidity = fields.Float(string="Total de liquidité", required=True)
    recovery_amount= fields.Float(string="Montant de récupération", required=True )
    real_liquidity = fields.Float(string="Solde Réel", required=True)
    solde_theoric = fields.Float(string="Solde Théorique", required=True)
    cash_difference = fields.Float(string="Ecart de caisse", compute="cash_dif")
    
    Commentaire = fields.Html(string="Commentaire")
    mode_payement = fields.Many2one(string="Mode de paiement", comodel_name="pos.payment.method", required=True)
    methode_payement_id = fields.Many2one(string="Mode de paiement", comodel_name="pos.payment.method", required=True)
    
    @api.depends("total_sale", "real_liquidity")
    def cash_dif(self):
            for rec in self:
                 rec.cash_difference = float(rec.real_liquidity - rec.total_sale)
            
    @api.depends("solde_theoric", "recovery_amount")
    def total_vente(self):
            for rec in self:
                rec.total_sale = float(rec.solde_theoric + rec.recovery_amount)

    # def name_get(self):
    #     result =[]
    #     for sexion_line in self:
    #         name ="["+ sexion_line.user_id + "]" + " " + sexion_line.sexion 
    #         result.append((sexion_line.id, name))
    #         return result
