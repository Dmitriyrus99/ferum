from frappe import _

def validate_service_request(doc, method):
    # нельзя закрыть без отчёта
    if doc.status in ("Выполнена", "Закрыта") and not doc.linked_report:
        frappe.throw(_("Нельзя закрыть заявку без привязанного Service Report"))

def handle_status_update(doc, method):
    """Если статус меняется на 'Отменена' — удаляем ссылку на отчёт"""
    if doc.status == "Отменена" and doc.linked_report:
        doc.db_set("linked_report", None, update_modified=False)

def prevent_deletion_with_links(doc, method):
    if doc.linked_report:
        frappe.throw(_("Нельзя удалить заявку: к ней привязан Service Report"))

def get_engineers_for_object(service_object):
    engineers = frappe.get_all(
        "AssignedEngineerItem",
        filters={"parent": service_object},
        pluck="engineer"          # поле Link на User
    )
    return engineers