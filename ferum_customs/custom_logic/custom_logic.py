import frappe

def update_linked_request_on_submit(doc, method):
    sr = frappe.get_doc('ServiceRequest', doc.service_request)
    sr.linked_report = doc.name
    sr.status = 'Выполнена'
    sr.save(ignore_permissions=True)
    frappe.db.commit()

def validate_service_request(doc, method):
    if doc.status == 'Закрыта' and not doc.linked_report:
        frappe.throw('Cannot close Service Request without linked report.')

def handle_status_update(doc, method):
    if frappe.db.get_value('ServiceRequest', doc.name, 'status') != doc.status:
        frappe.sendmail(
            recipients=[doc.customer],
            subject='Service Request Status Updated',
            message=f'Status updated to {doc.status}'
        )

def prevent_deletion_with_links(doc, method):
    if frappe.db.exists('Sales Invoice', {'service_request_ref': doc.name}):
        frappe.throw('Cannot delete Service Request linked to Sales Invoice.')

def calculate_total_payable_for_report(doc, method):
    total = sum([item.amount for item in doc.work_items])
    doc.total_payable = total

def prevent_object_deletion(doc, method):
    active = frappe.db.get_all('ServiceRequest', filters={'service_object_link': doc.name, 'status': ['!=', 'Закрыта']})
    if active:
        frappe.throw('Cannot delete Service Object linked to active Service Requests.')

def delete_attachment_file(doc, method):
    if doc.attachment_file:
        file_doc = frappe.get_doc('File', {'file_url': doc.attachment_file})
        if file_doc:
            frappe.delete_doc('File', file_doc.name, force=True)

def calculate_total_payable_for_payroll(doc, method):
    # Placeholder logic: sum of payroll components
    doc.total_payable = 0  # Fill with actual computation
