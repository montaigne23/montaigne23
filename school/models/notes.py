from odoo import api, fields, models, _


class schoolNotes(models.Model):
  #  _rec_name = 'name'
    _inherits = {'school.student':'student_id'}
    _name = 'school.notes'

    student_id = fields.Many2one(
        'school.student',
        ondelete='cascade',
        delegate=True,
    )
    coef = fields.Integer('Coef')
    note_S1 = fields.Integer('Sequence 1')
    note_S2 = fields.Integer('Sequence 2')
    note_T1 = fields.Integer('Trimestre 1')
    note_S3 = fields.Integer('Sequence 3')
    note_S4 = fields.Integer('Sequence 4')
    note_T2 = fields.Integer('Trimestre 2')
    note_S5 = fields.Integer('Sequence 5')
    note_S6 = fields.Integer('Sequence 6')
    note_T3 = fields.Integer('Trimestre 3')
    # type_note = fields.Integer('Note', required=True, tracking=True)

    # student_id = fields.Many2one(string='Eleve', comodel_name='school.student')
    # subject_ids = fields.Many2many(string='Matières', comodel_name='school.subject',
    #                                  relation='note_sub_rel',
    #                                  column1='note',
    #                                  column2='name')



