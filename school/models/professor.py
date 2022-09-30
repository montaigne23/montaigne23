from odoo import api, fields, models, _


class schoolProfessor(models.Model):
    
    _inherits = {'res.users': 'user_id'}
    _name = 'school.professor'
    user_id = fields.Many2one(
        'res.users',
        ondelete='cascade',
        delegate=True,
    )
    _rec_name = 'name'
    sexe = fields.Selection([('M', 'M'), ('F', 'F')], required=True, tracking=True)
    identity_card = fields.Char(string='Numero de carte identité', required=True, tracking=True)
    address = fields.Text(string='Adress')
    birthday = fields.Date(string='Date de Naissance', required=True, tracking=True)
    start_date = fields.Date(
        'Date', default=fields.Date.context_today, readonly=True)
    # email = fields.Char(string='Email')
    # phone = fields.Char(string='Téléphone')
    specialite_ids = fields.Many2many('school.subject', string="Spécialité(s)", required=True)
    
    state = fields.Selection(
        [('Vacataire', 'Vacataire'),
         ('Permanent', 'Permanent'),
         ('Fermé', 'Fermé')
        ], 'Status', default='Vacataire',
        help="vérifier le status de l'enseignant",
        readonly=True,
        tracking=True,
        copy=False)




    department_ids = fields.Many2many(comodel_name='school.department',
                                   relation='prof_dep_rel',
                                   column1='professor_name',
                                   column2='code')   
    
    subject_ids = fields.Many2many(comodel_name='school.subject',
                                   relation='prof_sub_rel',
                                   column1='prof_name',
                                   column2='name')   
    
    classroom_ids = fields.Many2many(string='Classes', comodel_name='school.classroom',
                                     relation='prof_class_rel',
                                     column1='f_name',
                                     column2='name')