import frappe

def update_linked_request_on_submit(doc, method):
    """После submit ServiceReport:
       1) записать ссылку в ServiceRequest.linked_report
       2) сменить статус заявки на 'Выполнена'
    """
    if not doc.service_request:
        return

    req = frappe.get_doc("ServiceRequest", doc.service_request)
    req.db_set("linked_report", doc.name, update_modified=False)
    if req.status not in ("Выполнена", "Закрыта"):
        req.db_set("status", "Выполнена", update_modified=False)
    frappe.db.commit()
