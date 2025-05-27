app_name = 'ferum_customs'
app_title = 'Ferum Customizations'
app_publisher = 'Your Name'
app_description = 'Ferum-specific customizations for ERPNext'
app_email = 'you@example.com'
app_license = 'MIT'

doc_events = {
    'ServiceReport': {
        'on_submit': 'ferum_customs.custom_logic.update_linked_request_on_submit',
        'validate': 'ferum_customs.ferum_customs.doctype.service_report.service_report.validate'
    },
    'ServiceRequest': {
        'validate': 'ferum_customs.custom_logic.validate_service_request',
        'on_update': 'ferum_customs.custom_logic.handle_status_update',
        'on_trash': 'ferum_customs.custom_logic.prevent_deletion_with_links'
    },
    'ServiceObject': {
        'on_trash': 'ferum_customs.custom_logic.prevent_object_deletion'
    },
    'PayrollEntryCustom': {
        'before_save': 'ferum_customs.custom_logic.calculate_total_payable_for_payroll'
    },
    'CustomAttachment': {
        'on_trash': 'ferum_customs.custom_logic.delete_attachment_file'
    },
    'ServiceProject': {
        'validate': 'ferum_customs.ferum_customs.doctype.service_project.service_project.validate'
    }
}

permission_query_conditions = {
    'ServiceRequest': 'ferum_customs.permissions.get_service_request_pqc'
}

notification_config = 'ferum_customs.notifications.get_notification_config'

fixtures = ['Custom Field', 'Role', 'Custom DocPerm']

after_install = 'ferum_customs.install.after_install'

fixtures.append({"dt": "Workflow", "filters": [["workflow_name", "=", "ServiceRequest Flow"]]})
