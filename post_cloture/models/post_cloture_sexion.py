
import time
from odoo import models, fields, api


class post_cloture_sexion(models.Model):
    _name = 'post_cloture.sexion'
    _description = 'post_cloture.sexion'
    _rec_name = 'date'
    date = fields.Datetime(default=fields.Datetime.now,
                           string="Date", required=True)
    commentaire = fields.Text(string="Descriptions",)
    status = fields.Selection([
        ("Nouveau", "Nouveau"), ("Valider", "Valider"), ("Cloturer", "Cloturer")
    ], 'Status', default='Nouveau',
        help="vérifié le status", tracking=True,
        copy=False, readonly=True,)
    post_cloture_sexion_line_ids = fields.One2many(
        comodel_name="post_cloture.sexion_line", inverse_name="sexion_id", string="Sexion line")
    post_cloture_sexion_synthese = fields.One2many(
        comodel_name="post_cloture.synthese", inverse_name="sexion_id", string="Synthese")
    montant_total_th = fields.Float(
        string="Montant total théorique", compute="montant_total_th_compute")
    total_reel = fields.Float(
        string="total reel", compute="total_reel_compute")
    ecart = fields.Float(string="Ecart", compute="ecart_compute")

    def Cloturer(self):
        self.status = "Cloturer"
        self.action_synthese_picking()

    def Charger(self):
        self.action_create_picking()
        self.status = "Valider"

    @api.depends("montant_total_th", "total_reel")
    def ecart_compute(self):
        for i in self:
            i.ecart = i.total_reel - i.montant_total_th

    @api.depends("post_cloture_sexion_line_ids")
    def total_reel_compute(self):
        for j in self:
            liqui = 0
            for line in j.post_cloture_sexion_line_ids:
                liqui += line.real_liquidity
            j.total_reel = j.total_reel + liqui

    @api.depends("post_cloture_sexion_line_ids")
    def montant_total_th_compute(self):
        for j in self:
            theo = 0
            for line in j.post_cloture_sexion_line_ids:
                theo += line.solde_theoric
            j.montant_total_th = j.montant_total_th + theo

        return True

    # @api.onchange('commentaire')
    # def test(self):
    #     z  = time.
    #     print(z)

        # def _prepare_cloture_line(self,sess,mode_payment,amount):

        # return {
        # 'user_id':sess.user_id.id,
        # 'sexion_id': sess.id,
        # 'date_start': sess.start_at,
        # 'date_close': sess.stop_at,
        # 'total_sale': amount,
        # 'recovery_amount': 0,
        # 'real_liquidity': 0,
        # 'solde_theoric': amount,
        # 'cash_difference': 0,
        # 'mode_payement': self.id,
        # }

    def action_create_picking(self):
        for order in self:
            today = order.date
            # session_obj = self.env['pos.session'].search([('start_at', '<=', today),('stop_at', '>=', today)],order = "start_at desc")
            session_obj = self.env['pos.session'].search(
                [('start_at', '<=', today), ('stop_at', '>=', today)], order="start_at")
            if session_obj:
                for sess in session_obj:
                    result = self.env['pos.payment'].read_group(
                        [('session_id', '=', sess.id)], ['amount'], ['session_id'])
                    session_amount_map = dict(
                        (data['session_id'][0], data['amount']) for data in result)
                    print('le truc la est', result)
                    for mode_payment in sess.config_id.payment_method_ids:
                        amount = 0
                        paiement = self.env['pos.payment'].search(
                            [('session_id', '=', sess.id), ('payment_method_id', '=', mode_payment.id)])
                        for line in paiement:
                            amount += line.amount

                    # res = order._prepare_cloture_line(sess,mode_payment,amount)
                        picking = self.env['post_cloture.sexion_line'].create({
                            'user_id': sess.user_id.id,
                            'sexion_id': order.id,
                            'date_start': sess.start_at,
                            'date_close': sess.stop_at,
                            # 'total_sale': amount,
                            'total_liquidity': amount,
                            'recovery_amount': 0,
                            'real_liquidity': 0,
                            'solde_theoric': amount,
                            'methode_payement_id': mode_payment.id,
                            'mode_payement': mode_payment.id,
                        }
                        )


    def action_synthese_picking(self):
        info_list = []
        methodeP_list = []

        for order in self:
            for i in order.post_cloture_sexion_line_ids:
                d = i.mode_payement.name
                rl = i.real_liquidity
                st = i.solde_theoric
                cd = rl - st
                print(d,rl,st,cd)
                if d in methodeP_list:
                     info_list[methodeP_list.index(
                            d)][0] = rl + info_list[methodeP_list.index(d)][0]
                     print(info_list[methodeP_list.index(d)][0])
                     info_list[methodeP_list.index(
                            d)][1] = st + info_list[methodeP_list.index(d)][1]
                     print(info_list[methodeP_list.index(d)][1])
                     info_list[methodeP_list.index(
                            d)][2] = cd + info_list[methodeP_list.index(d)][2]
                     print(info_list[methodeP_list.index(d)][2])
                else:
                     methodeP_list.append(d)
                     info_list.append([rl,st,cd])

                # if d :

                # else:
                #      i.cash_difference = rl - st
            for rec in methodeP_list:
                print('oki', rec, info_list[methodeP_list.index(rec)][1])
                pickings = self.env['post_cloture.synthese'].create({
                    'sexion_id': order.id,
                    'real_liquidity': info_list[methodeP_list.index(rec)][0],
                        'solde_theoric': info_list[methodeP_list.index(rec)][1],
                        'mode_payement': rec,
                        'cash_difference': info_list[methodeP_list.index(rec)][2]
                })
