/* /web/static/src/main.js defined in bundle 'web.assets_backend_prod_only' */
odoo.define("@web/main", async function (require) {
    "use strict";
    let __exports = {};
    const { startWebClient } = require("@web/start");
    const { WebClient } = require("@web/webclient/webclient");
    startWebClient(WebClient);
    return __exports;
});

/* /web/static/src/start.js defined in bundle 'web.assets_backend_prod_only' */
odoo.define("@web/start", async function (require) {
    "use strict";
    let __exports = {};
    const { makeEnv, startServices } = require("@web/env");
    const { legacySetupProm } = require("@web/legacy/legacy_setup");
    const { mapLegacyEnvToWowlEnv } = require("@web/legacy/utils");
    const { processTemplates } = require("@web/core/assets");
    const { session } = require("@web/session");
    const { mount, utils } = owl;
    const { whenReady } = utils;
    __exports.startWebClient = startWebClient;
    async function startWebClient(Webclient) {
        odoo.info = { db: session.db, server_version: session.server_version, server_version_info: session.server_version_info, isEnterprise: session.server_version_info.slice(-1)[0] === "e" };
        odoo.isReady = false;
        const env = makeEnv();
        const [, templates] = await Promise.all([startServices(env), odoo.loadTemplatesPromise.then(processTemplates)]);
        env.qweb.addTemplates(templates);
        await whenReady();
        const legacyEnv = await legacySetupProm;
        mapLegacyEnvToWowlEnv(legacyEnv, env);
        const root = await mount(Webclient, { env, target: document.body, position: "self" });
        odoo.__WOWL_DEBUG__ = { root };
        odoo.isReady = true;
        const favicon = `/web/image/res.company/${env.services.company.currentCompany.id}/favicon`;
        const icons = document.querySelectorAll("link[rel*='icon']");
        const msIcon = document.querySelector("meta[name='msapplication-TileImage']");
        for (const icon of icons) {
            icon.href = favicon;
        }
        if (msIcon) {
            msIcon.content = favicon;
        }
    }
    return __exports;
});

/* /web/static/src/legacy/legacy_setup.js defined in bundle 'web.assets_backend_prod_only' */
odoo.define("@web/legacy/legacy_setup", async function (require) {
    "use strict";
    let __exports = {};
    const { registry } = require("@web/core/registry");
    const { makeLegacyNotificationService, makeLegacyRpcService, makeLegacySessionService, makeLegacyDialogMappingService, makeLegacyCrashManagerService, makeLegacyCommandService, makeLegacyDropdownService } = require("@web/legacy/utils");
    const { makeLegacyActionManagerService } = require("@web/legacy/backend_utils");
    const AbstractService = require("web.AbstractService");
    const legacyEnv = require("web.env");
    const session = require("web.session");
    const makeLegacyWebClientService = require("web.pseudo_web_client");
    const { Component, config, utils } = owl;
    const { whenReady } = utils;
    let legacySetupResolver;
    const legacySetupProm = (__exports.legacySetupProm = new Promise((resolve) => {
        legacySetupResolver = resolve;
    }));
    (async () => {
        config.mode = legacyEnv.isDebug() ? "dev" : "prod";
        AbstractService.prototype.deployServices(legacyEnv);
        Component.env = legacyEnv;
        const legacyActionManagerService = makeLegacyActionManagerService(legacyEnv);
        const serviceRegistry = registry.category("services");
        serviceRegistry.add("legacy_action_manager", legacyActionManagerService);
        const legacyRpcService = makeLegacyRpcService(legacyEnv);
        serviceRegistry.add("legacy_rpc", legacyRpcService);
        const legacySessionService = makeLegacySessionService(legacyEnv, session);
        serviceRegistry.add("legacy_session", legacySessionService);
        const legacyWebClientService = makeLegacyWebClientService(legacyEnv);
        serviceRegistry.add("legacy_web_client", legacyWebClientService);
        serviceRegistry.add("legacy_notification", makeLegacyNotificationService(legacyEnv));
        serviceRegistry.add("legacy_crash_manager", makeLegacyCrashManagerService(legacyEnv));
        const legacyDialogMappingService = makeLegacyDialogMappingService(legacyEnv);
        serviceRegistry.add("legacy_dialog_mapping", legacyDialogMappingService);
        const legacyCommandService = makeLegacyCommandService(legacyEnv);
        serviceRegistry.add("legacy_command", legacyCommandService);
        serviceRegistry.add("legacy_dropdown", makeLegacyDropdownService(legacyEnv));
        await Promise.all([whenReady(), session.is_bound]);
        legacyEnv.qweb.addTemplates(session.owlTemplates);
        legacySetupResolver(legacyEnv);
    })();
    return __exports;
});
odoo.define(`web.legacySetup`, async function (require) {
    return require("@web/legacy/legacy_setup")[Symbol.for("default")];
});

/* /mail/static/src/main.js defined in bundle 'web.assets_backend_prod_only' */
odoo.define("@mail/main", async function (require) {
    "use strict";
    let __exports = {};
    const { ChatWindowService } = require("@mail/services/chat_window_service/chat_window_service");
    const { DialogService } = require("@mail/services/dialog_service/dialog_service");
    const { MessagingService } = require("@mail/services/messaging/messaging");
    const { SystrayService } = require("@mail/services/systray_service/systray_service");
    const { DiscussWidget } = require("@mail/widgets/discuss/discuss");
    const { action_registry } = require("web.core");
    const { serviceRegistry } = require("web.core");
    serviceRegistry.add("chat_window", ChatWindowService);
    serviceRegistry.add("dialog", DialogService);
    serviceRegistry.add("messaging", MessagingService);
    serviceRegistry.add("systray_service", SystrayService);
    action_registry.add("mail.widgets.discuss", DiscussWidget);
    return __exports;
});
