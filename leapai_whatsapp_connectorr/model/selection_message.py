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
from odoo import fields, models


class SelectionMessage(models.Model):
    """ Message Templates """
    _name = 'selection.message'
    _description = 'Selection Message'

    name = fields.Char(string="Name",
                       help="Name of message template")
    message = fields.Text(string="Message", required=True,
                          help="The message to send")
