from odoo import api, fields, models, _

class FacturationElem(models.Model):
    _name = 'open_transport.facturation'
    _rec_name = "debour_id"


    base = fields.Float(string="Base", compute="_compute_base")
    tax_id = fields.Many2many('account.tax', string='Taxes', context={'active_test': False})

    debour_id = fields.Many2one(comodel_name="product.product", string="Debour", ondelete='cascade',
        delegate=True,)
    dossier_id = fields.Many2one(comodel_name="open_transport.dossier", string="Dossier")

    quantite = fields.Integer(string="Quantité")
    MontHT = fields.Float(string="Montant hors taxe", compute="_compute_amount")
    taxe_price = fields.Float(string="Valeur de la Taxe", compute="_compute_amount", invisible=True)
    MontTC = fields.Float(string="Montant TTC", compute="_compute_amount")
    # @api.one
    # @api.depends('list_price','quantite','tax_id')
    # def _compute_MontHT(self):
    #     f = []
    #     j = 0
    #     for rec in self:
    #         rec.MontHT = rec.base * rec.quantite
    #         rec.MontTC = rec.MontHT
    #         for re in rec.tax_id:
    #             f.append((re.amount*rec.MontHT)/100)
    #         for i in f: 
    #             rec.MontTC = i + rec.MontTC
    
    @api.depends('debour_id')
    def _compute_base(self):
        for rec in self:
            rec.base = rec.debour_id.list_price
            rec.tax_id = rec.debour_id.taxes_id
            
    @api.onchange('debour_id')
    def _update_tax(self):
        for rec in self:
            rec.tax_id = rec.debour_id.taxes_id


    @api.depends('quantite', 'base', 'tax_id')
    def _compute_amount(self):
        """
        Compute the amounts of the SO line.
        """
        for line in self:
            price = line.base
            taxes = line.tax_id.compute_all(price, line.dossier_id.currency_id, line.quantite, product=line.debour_id, partner=line.dossier_id.client_id)
            line.update({
                'taxe_price': sum(t.get('amount', 0.0) for t in taxes.get('taxes', [])),
                'MontTC': taxes['total_included'],
                'MontHT': taxes['total_excluded'],
            })
