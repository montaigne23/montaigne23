from odoo import api, fields, models, _


class schoolSubject(models.Model):
    _name = 'school.subject'
    _rec_name = 'name'
    name = fields.Char(string='Nom Matière' ,required=True, tracking=True)
    coef = fields.Integer(string='Coef' ,required=True, tracking=True)
    code = fields.Char(string='Code', required=True, copy=False, readonly=True,
                            index=True, default=lambda self: _('New'))

    department_id = fields.Many2one(string='département' ,comodel_name='school.department')

    classroom_ids = fields.Many2many(string='Classes' ,comodel_name='school.classroom',
                                     relation='sub_class_rel',
                                     column1='name',
                                     column2='classroom_name')
    professor_ids = fields.Many2many( comodel_name='school.professor',
                                     relation='sub_prof_rel',
                                     column1='name',
                                     column2='prof_name')



    @api.model
    def create(self, vals):
        if vals.get('code', _('New')) == _('New'):
            vals['code'] = self.env['ir.sequence'].next_by_code('school.subject.sequence') or _('New')
        result = super(schoolSubject, self).create(vals)
        
        return result


