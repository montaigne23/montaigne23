from odoo import models, fields, api


class post_cloture_sexion_synthese(models.Model):
    
    # _inherits = {'res.user':'user_id'}
    _name = 'post_cloture.synthese'
    _description = 'post_cloture.synthese'
    
    mode_payement = fields.Char(string="Mode de paiement", required=True, readonly=True)
    real_liquidity = fields.Float(string="Solde Réel", required=True, readonly=True)
    solde_theoric = fields.Float(string="Solde Théorique", required=True, readonly=True)
    cash_difference = fields.Float(string="Ecart de caisse", readonly=True)

    sexion_id = fields.Many2one(string="Sexion",
                             comodel_name='post_cloture.sexion',
                             required=False,invisible=True
                              )

