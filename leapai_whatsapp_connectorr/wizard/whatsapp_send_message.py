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
from odoo import api, fields, models


class WhatsappSendMessage(models.TransientModel):
    """ Wizard for sending whatsapp message."""
    _name = 'whatsapp.send.message'
    _description = 'Whatsapp Send Message'

    partner_id = fields.Many2one('res.partner',
                                 string="Recipient",
                                 help="Partner")
    mobile = fields.Char(string="Contact Number",
                         required=True,
                         help="Contact number of Partner")
    message = fields.Text(string="Message",
                          required=True,
                          help="Message to send")
    image_1920 = fields.Binary(string='Image', help="Image of Partner")

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        """ Function for fetching the mobile number and image of partner."""
        self.mobile = self.partner_id.mobile
        self.image_1920 = self.partner_id.image_1920

    def send_message(self):
        """ This function redirects to the whatsapp web with required
        parameters.
        """
        if self.message and self.mobile:
            message_string = ''
            message = self.message.split(' ')
            for msg in message:
                message_string = message_string + msg + '%20'
            message_string = message_string[:(len(message_string) - 3)]
            message_post_content = message_string
            if self.partner_id:
                self.partner_id.message_post(body=message_post_content)
            return {
                'type': 'ir.actions.act_url',
                'url': "https://api.whatsapp.com/send?phone=" + self.mobile +
                       "&text=" + message_string,
                'target': 'new',
                'res_id': self.id,
            }
