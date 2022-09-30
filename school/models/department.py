from odoo import api, fields, models, _


class schoolDepartment(models.Model):
    _name = 'school.department'
    _rec_name = 'name'
    name = fields.Char(string='Nom', required=True, tracking=True)
    code = fields.Char(string='Code', required=True, copy=False, readonly=True,
                            index=True, default=lambda self: _('New'))

    professor_ids = fields.Many2many(comodel_name='school.professor',
                                   relation='dep_prof_rel',
                                   column1='code',
                                   column2='professor_name')   
    
    subject_ids = fields.One2many(string='Matières', comodel_name='school.subject', inverse_name='department_id')


    @api.model
    def create(self, vals):
        if vals.get('code', _('New')) == _('New'):
            vals['code'] = self.env['ir.sequence'].next_by_code('school.department.sequence') or _('New')
        result = super(schoolDepartment, self).create(vals)
        
        return result

