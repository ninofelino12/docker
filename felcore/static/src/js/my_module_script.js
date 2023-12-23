odoo.define('my_module.my_module_script', function (require) {
    'use strict';

    var core = require('web.core');
    var Widget = require('web.Widget');
    var rpc = require('web.rpc');

    var QWeb = core.qweb;

    var MyModuleWidget = Widget.extend({
        template: 'my_module_template',
        events: {
            'click #add_partner': 'addPartner',
        },
        init: function (parent) {
            this._super.apply(this, arguments);
            this.partnerList = [];
        },
        start: function () {
            this.$el.appendTo('#wrapwrap');  // Ganti dengan elemen yang sesuai
            this.renderPartnerList();
            return this._super();
        },
        renderPartnerList: function () {
            var self = this;
            var $partnerList = this.$('#partner_list');
            $partnerList.empty();

            rpc.query({
                model: 'res.partner',
                method: 'search_read',
                args: [[]],
                fields: ['id', 'name'],
            }).then(function (partners) {
                self.partnerList = partners;
                partners.forEach(function (partner) {
                    var $partnerItem = $('<li>').text(partner.name);
                    $partnerList.append($partnerItem);
                });
            });
        },
        addPartner: function () {
            var self = this;
            var partnerName = this.$('#partner_name').val();

            rpc.query({
                model: 'res.partner',
                method: 'create',
                args: [{ 'name': partnerName }],
            }).then(function (partnerId) {
                self.renderPartnerList();
                self.$('#partner_name').val('');
            });
        },
    });

    core.action_registry.add('my_module_action', MyModuleWidget);

    return MyModuleWidget;
});
