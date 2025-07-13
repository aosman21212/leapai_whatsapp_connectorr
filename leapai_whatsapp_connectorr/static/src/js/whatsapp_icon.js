/** @odoo-module **/

import { registry } from "@web/core/registry";
import { SystrayMenu } from "@web/webclient/systray/systray_menu";

export class WhatsappIcon extends SystrayMenu {
    setup() {
        super.setup();
    }

    async onClick() {
        // WhatsApp functionality
        const phoneNumber = "+1234567890"; // Default phone number
        const message = "Hello from Odoo!"; // Default message
        const whatsappUrl = `https://wa.me/${phoneNumber}?text=${encodeURIComponent(message)}`;
        window.open(whatsappUrl, '_blank');
    }
}

WhatsappIcon.template = 'leapai_whatsapp_connectorr.whatsapp_icon';
registry.category("systray").add("whatsapp_icon", WhatsappIcon);
