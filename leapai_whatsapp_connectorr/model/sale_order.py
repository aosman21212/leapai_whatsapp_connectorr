# -*- coding: utf-8 -*-
#############################################################################
#
#    LeapAI
#
#    Copyright (C) 2024-TODAY LeapAI
#    Author: LeapAI Team
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
from itertools import groupby
from odoo import models, _
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    """
    This class extends the 'sale.order' model to add custom functionalities
    related to WhatsApp messaging.
    """
    _inherit = 'sale.order'

    def action_send_whatsapp(self):
        """Send WhatsApp message for sale order"""
        self.ensure_one()
        return {
            'name': 'Send WhatsApp Message',
            'type': 'ir.actions.act_window',
            'res_model': 'whatsapp.send.message',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_res_model': 'sale.order',
                'default_res_id': self.id,
                'default_template_id': self.env.ref(
                    'leapai_whatsapp_connectorr.whatsapp_send_message_view_form').id
            }
        }

    def action_send_mail(self):
        """Send email for sale order"""
        self.ensure_one()
        return {
            'name': 'Send Email',
            'type': 'ir.actions.act_window',
            'res_model': 'mail.compose.message',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_model': 'sale.order',
                'default_res_id': self.id,
                'default_template_id': self.env.ref(
                    'leapai_whatsapp_connectorr.whatsapp_send_message_view_form').id
            }
        }

    def check_customers(self, partner_ids):
        """ Check if the selected sale orders belong to the same customer."""
        partners = groupby(partner_ids)
        return next(partners, True) and not next(partners, False)

    def action_whatsapp_multi(self):
        """
        Initiate WhatsApp messaging for multiple sale orders and open a message
        composition wizard.
        """
        sale_order_ids = self.env['sale.order'].browse(
            self.env.context.get('active_ids'))
        partner_ids = []
        for sale in sale_order_ids:
            partner_ids.append(sale.partner_id.id)
        partner_check = self.check_customers(partner_ids)
        if partner_check:
            sale_numbers = sale_order_ids.mapped('name')
            sale_numbers = "\n".join(sale_numbers)
            compose_form_id = self.env.ref(
                'whatsapp_mail_messaging.whatsapp_send_message_view_form').id
            ctx = dict(self.env.context)
            message = ("Hi" + " " + self.partner_id.name + ',' + '\n' +
                       "Your Orders are" + '\n' + sale_numbers + ' ' + '\n' +
                       "is ready for review.Do not hesitate to contact us if "
                       "you have any questions.")
            ctx.update({
                'default_message': message,
                'default_partner_id': sale_order_ids[0].partner_id.id,
                'default_mobile': sale_order_ids[0].partner_id.mobile,
                'default_image_1920': sale_order_ids[0].partner_id.image_1920,
            })
            return {
                'type': 'ir.actions.act_window',
                'view_mode': 'form',
                'res_model': 'whatsapp.send.message',
                'views': [(compose_form_id, 'form')],
                'view_id': compose_form_id,
                'target': 'new',
                'context': ctx,
            }
        else:
            raise UserError(_(
                'It appears that you have selected orders from multiple'
                ' customers. Please select orders from a single customer.'))
