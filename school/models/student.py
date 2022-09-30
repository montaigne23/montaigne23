import datetime
from odoo import api, fields, models, _


class schoolStudent(models.Model):
    _inherits = {'res.users': 'user_id'}
    user_id = fields.Many2one(
        'res.users',
        ondelete='cascade',
        delegate=True,
    )

    _name = 'school.student'
    # _rec_name = 'f_name'
    
    matricule = fields.Char(string='Matricule', required=True, copy=False, readonly=True,
                            index=True, default=lambda self: _(' '))
    # f_name = fields.Char(string='Nom', required=True, tracking=True)
    # l_name = fields.Char(string='Prenom', required=True, tracking=True)
    sexe = fields.Selection([('Male', 'Male'), ('Female', 'Female')], required=True, tracking=True)
    f_name_mere = fields.Char(string='Nom de la mère')
    f_name_pere = fields.Char(string='Nom du père', required=True, tracking=True)
    identity_card = fields.Char(string='Numero de carte identité si possible')
    # address = fields.Text(string='Address', required=True, tracking=True)
    birthday = fields.Date(string='Date de Naissance', required=True, tracking=True)
    registration_date = fields.Datetime(
        'Date', default=fields.Datetime.now, tracking=True, readonly=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Téléphone', default=lambda self: _('+2376'))
    address_parent = fields.Text(string='Address', required=True, tracking=True)
    email_parent = fields.Char(string='Email')
    phone_parent1 = fields.Char(string='tel/whatsapp 1', required=True, tracking=True, default=lambda self: _('+2376'))
    phone_parent2 = fields.Char(string='tel/whatsapp 2', default=lambda self: _('+2376'))

    nbr_redouble = fields.Integer(string='quantième année ?', required=True)
    situation_eleve = fields.Selection( [("Nouveau", "Nouveau"),("Redoublant", "Redoublant")], string='Situation', required=True)
    type_eleve = fields.Selection( [("Régulier", "Régulier"),("Irrégulier", "Irrégulier")], string='Type', required=True)
    department_id = fields.Many2one(string='département', comodel_name='school.department', required=True)
    classroom_id = fields.Many2one(string='Classe', comodel_name='school.classroom',required=True)
    # note_ids = fields.One2many(string='Notes', comodel_name='school.notes',inverse_name='student_id')
    state_physic = fields.Selection(
        [("Apte", "Apte"), ("Inapte", "Inapte")], string=" Status", required=True, tracking=True)
    state = fields.Selection(
        [('Enregistrement', 'Enregistrement'),
         ('Inscription', 'Inscription'),
         ('Tranche 1', 'Tranche 1'),
         ('Tranche 2', 'Tranche 2'),
         ('Solvable', 'Solvable')
        ], 'Status', default='Enregistrement', readonly=True,
        help="vérifié la solvabilité de l'elève",
        tracking=True,
        copy=False)

    # @api.multi
    def name_get(self):
        result =[]
        for student in self:
            name ="["+ student.matricule + "]" + " " + student.name
            result.append((student.id, name))
            return result

    @api.model
    def create(self, vals):
        if vals.get('matricule', _(' ')) == _(' '):
            vals['matricule'] = self.env['ir.sequence'].next_by_code('school.student.sequence') or _(' ')
        result = super(schoolStudent, self).create(vals)
        
        return result
    
    # @api.model
    # def compute_password(self):
    #     for user in self:
    #         user.password = user.matricule

    # def currentDatetime(self):
    #     if self.registration_date:
    #         self.registration_date=self.registration_date
    #     else: 
    #         self.registration_date = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')