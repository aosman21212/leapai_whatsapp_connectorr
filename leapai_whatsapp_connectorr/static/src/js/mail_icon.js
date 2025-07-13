/** @odoo-module **/

import { registry } from "@web/core/registry";
import { SystrayMenu } from "@web/webclient/systray/systray_menu";

export class MailButton extends SystrayMenu {
    setup() {
        super.setup();
    }

    async onClick() {
        // Mail functionality
        const subject = "Message from Odoo";
        const body = "Hello from Odoo!";
        const mailtoUrl = `mailto:?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
        window.open(mailtoUrl, '_blank');
    }
}

MailButton.template = 'leapai_whatsapp_connectorr.mail_icon';
registry.category("systray").add("mail_icon", MailButton);
