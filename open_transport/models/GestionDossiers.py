from email.policy import default
from odoo import api, fields, models, _

class DossiersManagers(models.Model):
    
    _name ='open_transport.dossier'
    _rec_name = 'client_id'
    code = fields.Char(string='Matricule', required=True, copy=False, readonly=True,
                            index=True, default=lambda self: _(' '))
    image_1920 = fields.Image("Logo", max_width=228, max_height=228, compute="_compute_img")
    tajets_ids = fields.One2many(comodel_name='open_transport.trajets_list_custom', inverse_name="dossier_id")
    cout = fields.Float(compute="comp_cout", invisible=True)
    cout_compute_currence = fields.Char(String="Cout", compute="currence_cout")
    currency_id = fields.Many2one(related='client_id.currency_id', depends=["client_id"], store=True, ondelete="restrict")
    client_id = fields.Many2one(comodel_name='res.partner',  string='Client',required=True, tracking=True)
    facturation_elem_ids = fields.One2many(comodel_name="open_transport.facturation", inverse_name="dossier_id")
    partner_ids = fields.One2many(comodel_name="open_transport.res_partner", inverse_name="dossier_id")
    num_ref = fields.Char(string="Numero de Reference", required=True)
    pays_des = fields.Many2one(comodel_name="res.country" ,string="Pays destination",required=True)
    embarquement_port = fields.Char(string="Port d'embarquement")
    debarquement_port = fields.Char(string="Port debarquement")
    company_mari = fields.Char(string="Compagnie maritime",required=True)
    trasit_order = fields.Char(string="Ordre de transit",required=True)
    Navire = fields.Char(string="Navire",required=True)
    etat_navire = fields.Char(string="Etat du navire")
    eta = fields.Char(string="ETA")
    destinataire = fields.Char(string="Destinataire",required=True)
    notify = fields.Char(string="Notify")
    declaration = fields.Char(string="Déclaration")
    declaration_date = fields.Datetime(default=fields.Datetime.now,string="Date de déclaration",required=True)
    state_date = fields.Datetime(default=fields.Datetime.now,string="Date d'ouverture",required=True)
    contrat = fields.Char(string="Contrat",required=True)
    fac_num = fields.Char(string="Numero de la facture")
    facturation = fields.Char(string="Facturation")
    observation = fields.Html(string="Observation")
    frais_fixe_dossier = fields.Float(string="Frais fixe du dossier")
    had = fields.Char(string="Honoraire d'agrée en douane")
    taxe_TVA = fields.Float(string="TVA", default=lambda self: _(19.25), readonly=True)
    total_HT = fields.Float(string="Total hors taxe", compute="_total__values",invisible=True)
    total_HT_curr = fields.Float(string="Total hors taxe", compute="_total__values")
    taxe_values = fields.Float(string="Valeur de la Taxe", compute="_taxe_values")
    total_TTC = fields.Float(string="Total TTC", compute="_total__values", invisible=True)
    total_gen = fields.Float(string="Total générale", compute="_total__gen", invisible=True)
    total_gen_curr = fields.Float(string="Total générale", compute="")
    none =fields.Char(string=" ", readonly=True)

    @api.depends('partner_ids','tajets_ids')
    def comp_cout(self):
        for rec in self:
            rec.cout = 0
            for cout in rec.tajets_ids :
                rec.cout = cout.trajet_id.amende + rec.cout
            for couts in rec.partner_ids :
                rec.cout = couts.Cout + rec.cout
    
    @api.depends('cout')
    def currence_cout(self):
        for rec in self :
            rec.cout_compute_currence =  str(rec.cout) + " " +"FCFA"
    
    @api.model
    def create(self, vals):
        if vals.get('code', _(' ')) == _(' '):
            vals['code'] = self.env['ir.sequence'].next_by_code('open_transport.dossier.sequence') or _(' ')
        result = super(DossiersManagers, self).create(vals)
        
        return result

    def _compute_tva(self):
        for rec in self:
            rec.taxe_TVA = 19.25

    @api.depends('client_id')
    def _compute_img(self):
        for rec in self:
            rec.image_1920 = rec.client_id.image_1920
            
    @api.depends('facturation_elem_ids')
    def _total__values(self):
        self.total_HT =0
        self.total_TTC =0
        self.taxe_values = 0
        for rec in self.facturation_elem_ids:
            self.total_HT = rec.MontHT + self.total_HT
            self.total_TTC = rec.MontTC + self.total_TTC
            self.taxe_values = rec.taxe_price + self.taxe_values
            
            
    # @api.depends('total_HT', 'total_TTC')
    # def _taxe_values(self):
    #     for rec in self:
    #             rec.taxe_values = rec.total_TTC - rec.total_HT
    
    @api.depends('frais_fixe_dossier','total_TTC')
    def _total__gen(self):
        self.total_gen = self.total_TTC + self.frais_fixe_dossier
        
    