
#from pkg_resources import require
from odoo import api, fields, models, _


class schoolClassroom(models.Model):
    _name = 'school.classroom'
    _rec_name = 'classroom_name'
    
    
    classroom_name = fields.Char(string='Nom',  required=True, tracking=True)
    code = fields.Char(string='Code',  required=True, tracking=True)
    num_prof = fields.Integer(string='Nombre de Professeurs', compute='comp_prof')
    num_sub = fields.Integer(string='Nombre de Matières', compute='comp_sub')
    num_stu = fields.Integer(string="Nombre d'étudiants", compute='comp_stu')




    student_ids = fields.One2many(comodel_name='school.student', inverse_name='classroom_id')

    professor_ids = fields.Many2many(comodel_name='school.professor',
                                     relation='class_prof_rel',
                                     column1='name',  
                                     column2='f_name')
    subject_ids = fields.Many2many(comodel_name='school.subject',
                                   relation='class_sub_rel',
                                   column1='classroom_name',
                                   column2='name')   
    

    def comp_prof(self):
        self.num_prof = len(self.professor_ids)

    def comp_sub(self):
        self.num_sub = len(self.subject_ids)

    def comp_stu(self):
        self.num_stu = len(self.student_ids)
