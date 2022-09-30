from odoo import api, fields, models, _


class GestionTrajets(models.Model):
    _name = 'open_transport.gestiontrajets'
    _rec_name = 'name'

    name = fields.Char(invisible=True, compute='name_getter')
    code = fields.Char(string='Matricule', required=True, copy=False, readonly=True,
                            index=True, default=lambda self: _(' '))

    depard = fields.Many2one(string='Point de Dépard', required=True, tracking=True, comodel_name='open_transport.villes')
    arrive = fields.Many2one(string="Point d'arrivé", required=True, tracking=True, comodel_name='open_transport.villes')
    amende = fields.Float(string='Coût', required=True, tracking=True)
    amende_frais = fields.Float(string='Frais de Route', required=True, tracking=True)
    carburant_prix_unitaire = fields.Float(string='Prix Unitaire Carburant', required=True, tracking=True)
    quantites = fields.Float(string='Quantité carburant (litre)', required=True, tracking=True)
    MtTotal = fields.Float(string='Montant Total Carburant', compute='mont_total')
    duree_trajet = fields.Integer(string='Durée du Trajet (Heures)', required=True, tracking=True)
    
    # @api.depends('depard','arrive')
    def name_getter(self):
        for trajet in self:
            trajet.name = trajet.depard.name  + ">>>" + trajet.arrive.name

    @api.model
    def create(self, vals):
        if vals.get('code', _(' ')) == _(' '):
            vals['code'] = self.env['ir.sequence'].next_by_code('open_transport.gestiontrajets.sequence') or _(' ')
        result = super(GestionTrajets, self).create(vals)
        
        return result

    @api.onchange('quantites')
    def mont_total(self):
        self.MtTotal = self.carburant_prix_unitaire * self.quantites
        