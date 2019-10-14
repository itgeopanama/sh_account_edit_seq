# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

from odoo import fields,models,api
                    
class AccountInvoice(models.Model):
    _inherit = 'account.invoice'
    
    account_edit_sequence = fields.Boolean("Account Edit Sequence ?",default=False,compute ='account_edit_sequence_number_group')
    new_accnt_sequence = fields.Char("New Sequence", store=True)
    
    @api.one
    @api.depends('number')
    def account_edit_sequence_number_group(self):
        if self:
            if self.number == False:
                self.account_edit_sequence = False 
            else :  
                if self.user_has_groups('sh_edit_sequence_no.group_account_invoice_edit_sequence'): 
                    self.account_edit_sequence = True
                else:        
                    self.account_edit_sequence = False 
    
    @api.multi
    def action_invoice_open(self):
        res = super(AccountInvoice,self).action_invoice_open()
        if self.type == 'out_invoice': 
            accnt_seq = self.env['ir.sequence'].next_by_code('account.invoice') or _('New')
            self.new_accnt_sequence = accnt_seq
            self.move_id.new_name = accnt_seq
        if self.type == 'out_refund':
            accnt_seq = self.env['ir.sequence'].next_by_code('account.invoice.refund') or _('New')
            self.new_accnt_sequence = accnt_seq
            self.move_id.new_name = accnt_seq
        return res
    
    
        

# class AccountMove(models.Model):
#     _inherit = "account.move"   
#     
#     new_move_sequence = fields.Char(compute='_get_seq', string="New Sequence", readonly=False)
#     
#     @api.multi
#     def _get_seq(self):
#         if self:
#             for rec in self:
#                 new_seq = self.env['account.invoice'].search([('number','=',rec.name)],limit=1)
#                 rec.new_move_sequence = new_seq.new_accnt_sequence         
        
        
        