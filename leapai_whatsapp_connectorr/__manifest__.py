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
{
    'name': 'LeapAI WhatsApp Connector',
    'version': '18.0.1.0.0',
    'category': 'Extra Tools',
    'summary': """LeapAI WhatsApp Connector, WhatsApp Odoo Integration, Odoo WhatsApp Connector, 
     Odoo WhatsApp, WhatsApp Connector, WhatsApp Integration, Odoo18, WhatsApp,
     Odoo Apps, LeapAI""",
    'description': """Added options for sending WhatsApp messages and emails in 
     the systray bar, sale order, invoices, website portal view and ability to 
     share access URLs for documents through the share option available in each
     record using WhatsApp Web.""",
    'author': 'LeapAI',
    'company': 'LeapAI',
    'maintainer': 'LeapAI',
    'website': 'https://www.leapai.com',
    'depends': ['sale', 'account', 'website', 'sale_management'],
    'data': [
        'security/ir.model.access.csv',
        'views/website_templates.xml',
        'views/sale_order_views.xml',
        'views/account_move_views.xml',
        'views/website_views.xml',
        'views/selection_message_views.xml',
        'views/res_config_settings_views.xml',
        'wizard/whatsapp_send_message_views.xml',
        'wizard/portal_share_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            "leapai_whatsapp_connectorr/static/src/css/icons.css",
            "leapai_whatsapp_connectorr/static/src/js/whatsapp_icon.js",
            "leapai_whatsapp_connectorr/static/src/js/mail_icon.js",
            'leapai_whatsapp_connectorr/static/src/xml/whatsapp_icon_template.xml',
            'leapai_whatsapp_connectorr/static/src/xml/mail_icon_template.xml',
        ],
        'web.assets_frontend': [
            "leapai_whatsapp_connectorr/static/src/css/whatsapp_icon_website.css",
            "leapai_whatsapp_connectorr/static/src/js/whatsapp_web_icon.js",
            "leapai_whatsapp_connectorr/static/src/js/whatsapp_modal.js",
        ],
    },
    'images': ['static/description/banner.jpg'],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
