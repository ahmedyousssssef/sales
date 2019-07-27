# -*- coding: utf-8 -*-
import re
from openerp.osv import osv

from openerp import models, fields, api , _

# class sales_customiz(models.Model):
#     _name = 'sales_customiz.sales_customiz'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    date_original = fields.Date(string="Date Original",)
    source = fields.Selection(selection_add=[('email', 'Email') , ('instagram', 'Instagram')])

    broker_name = fields.Char(string="Broker Name")
    broker_mobil = fields.Char(string="Broker Mobile")


    # def create(self,cr,uid,vals,context=None):
    #     if 'broker_name' in vals and vals['broker_name']:
    #         if re.match("  ", vals['broker_name']) != None:
    #             pass
    #         else:
    #             raise osv.except_osv(_('Invalid Broker Name'), _('Please enter a validBroker Name'))
    #     return super(CrmLead, self).create(cr, uid,vals, context=context)
    #
    # @api.multi
    # def write(self, vals):
    #     if 'broker_name' in vals and vals['broker_name']:
    #         if re.match("  *$", vals['broker_name']) != None:
    #             pass
    #         else:
    #             raise osv.except_osv(_('Invalid Broker Name'), _('Please enter a valid Broker Name'))
    #     return super(CrmLead, self).write(vals)



    def create(self, cr, uid, vals, context=None):
        context = dict(context or {})
        if vals.get('type') and not context.get('default_type'):
            context['default_type'] = vals.get('type')
        if vals.get('team_id') and not context.get('default_team_id'):
            context['default_team_id'] = vals.get('team_id')
        if vals.get('user_id') and 'date_open' not in vals:
            vals['date_open'] = fields.datetime.now()

        if 'broker_name' in vals and vals['broker_name']:
            if re.match("^(?!.* {2})[a-zA-Z0-9][a-zA-Z0-9 ]+[a-zA-Z0-9]$", vals['broker_name']) != None:
                pass
            else:
                raise osv.except_osv(_('Invalid Broker Name'), _('Please enter a valid Broker Name'))

        if 'broker_mobil' in vals and vals['broker_mobil']:
            if re.match("^(?:\+?88)?01[0-9]\d{8}$", vals['broker_mobil']) != None:
                pass
            else:
                raise osv.except_osv(_('Invalid Broker Mobile Number'), _('Please enter a valid Broker Mobile Number'))
        # context: no_log, because subtype already handle this
        create_context = dict(context, mail_create_nolog=True)
        return super(CrmLead, self).create(cr, uid, vals, context=create_context)

    def write(self, cr, uid, ids, vals, context=None):
        # stage change: update date_last_stage_update
        if 'stage_id' in vals:
            vals['date_last_stage_update'] = fields.datetime.now()
        if vals.get('user_id') and 'date_open' not in vals:
            vals['date_open'] = fields.datetime.now()
        # stage change with new stage: update probability and date_closed
        if vals.get('stage_id') and 'probability' not in vals:
            onchange_stage_values = self.onchange_stage_id(cr, uid, ids, vals.get('stage_id'), context=context)['value']
            vals.update(onchange_stage_values)
        if vals.get('probability') >= 100 or not vals.get('active', True):
            vals['date_closed'] = fields.datetime.now()
        elif 'probability' in vals and vals['probability'] < 100:
            vals['date_closed'] = False

        if 'broker_name' in vals and vals['broker_name']:
            if re.match("^(?!.* {2})[a-zA-Z0-9][a-zA-Z0-9 ]+[a-zA-Z0-9]$", vals['broker_name']) != None:
                pass
            else:
                raise osv.except_osv(_('Invalid Broker Name'), _('Please enter a valid Broker Name'))

        if 'broker_mobil' in vals and vals['broker_mobil']:
            if re.match("^(?:\+?88)?01[0-9]\d{8}$", vals['broker_mobil']) != None:
                pass
            else:
                raise osv.except_osv(_('Invalid Broker Mobile Number'),
                                     _('Please enter a valid Broker Mobile Number'))
        return super(CrmLead, self).write(cr, uid, ids, vals, context=context)
