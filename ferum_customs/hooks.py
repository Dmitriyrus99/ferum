app_name = 'ferum_customs'
app_title = 'Ferum Customizations'
app_publisher = 'Ferum LLC'
app_description = 'Ferum-specific customizations for ERPNext'
app_email = 'support@ferum.ru'
app_license = 'MIT'

# ───────────────────────────────────────── doc_events ──────────────────────────────────────────
doc_events = {
    "ServiceReport": {
        # привязываем обработчик, который проставляет link и статус в заявке
        "on_submit": "ferum_customs.custom_logic.service_report_hooks.update_linked_request_on_submit",
        # доп. серверные валидации отчёта
        "validate": "ferum_customs.custom_logic.service_report_hooks.validate_service_report",
    },
    "ServiceRequest": {
        "validate": "ferum_customs.custom_logic.service_request_hooks.validate_service_request",
        "on_update": "ferum_customs.custom_logic.service_request_hooks.handle_status_update",
        "on_trash": "ferum_customs.custom_logic.service_request_hooks.prevent_deletion_with_links",
    },
    "ServiceObject": {
        "on_trash": "ferum_customs.custom_logic.service_object_hooks.prevent_object_deletion",
    },
    "PayrollEntryCustom": {
        "before_save": "ferum_customs.custom_logic.payroll_entry_hooks.calculate_total_payable",
    },
    "CustomAttachment": {
        "on_trash": "ferum_customs.custom_logic.attachment_hooks.delete_attachment_file",
    },
    "ServiceProject": {
        "validate": "ferum_customs.custom_logic.service_project_hooks.validate_service_project",
    },
}

# ───────────────────────────────── permission queries / notifications ──────────────────────────
permission_query_conditions = {
    "ServiceRequest": "ferum_customs.permissions.service_request_permissions.get_permission_query_conditions",
}

notification_config = "ferum_customs.notifications.config.get_notification_config"

# ─────────────────────────────────────────── fixtures ──────────────────────────────────────────
fixtures = [
    # любые Custom Field-ы, созданные в UI
    {"dt": "Custom Field"},

    # роли приложения
    {"dt": "Role", "filters": [["role_name", "in", [
        "Проектный менеджер",
        "Офис-менеджер",
        "Инженер",
        "Заказчик"
    ]]]},

    # индивидуальные права (если будут настроены через Role Permissions Manager)
    {"dt": "Custom DocPerm"},

    # workflow заявки
    {"dt": "Workflow", "filters": [["workflow_name", "=", "ServiceRequest Flow"]]},
]

# ────────────────────────────────────────── after_install ──────────────────────────────────────
after_install = "ferum_customs.after_install.after_install"
