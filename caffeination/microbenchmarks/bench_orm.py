from functools import lru_cache

import frappe
from frappe.desk.reportview import get, get_count


def bench_get_doc():
	return [frappe.get_doc("Role", r) for r in get_all_roles()]


def bench_get_user():
	"""Complex version of get_doc - involves child documents to init"""
	guest = frappe.get_doc("User", "Guest")
	admin = frappe.get_doc("User", "Administrator")
	return guest, admin


def bench_get_cached_doc():
	docs = []
	for role in get_all_roles():
		doctype = "Role"

		docs.append(frappe.get_cached_doc(doctype, role))

	# Clear "local" cache to avoid testing basically nothing.
	frappe.local.cache.clear()
	return docs


def bench_get_local_cached_doc():
	docs = []
	for role in get_all_roles():
		doctype = "Role"
		docs.append(frappe.get_cached_doc(doctype, role))
	return docs


def bench_get_all():
	return frappe.get_all("DocField", "*", limit=1, run=0)


def bench_get_list():
	return frappe.get_list("Role", "*", limit=20, run=0)


def bench_list_view_query():
	frappe.local.form_dict = {
		"doctype": "Role",
		"fields": '["`tabRole`.`name`","`tabRole`.`owner`","`tabRole`.`creation`","`tabRole`.`modified`","`tabRole`.`modified_by`" ,"`tabRole`.`_user_tags`","`tabRole`.`_comments`","`tabRole`.`_assign`","`tabRole`.`_liked_by`","`tabRole`.`docstatus`","`tabRole`.`idx`","`tabRole`.`disabled`"]',
		"filters": "[]",
		"order_by": "`tabRole`.creation desc",
		"start": "0",
		"page_length": "20",
		"group_by": "",
		"with_comment_count": "1",
	}
	return get()


def bench_get_all_with_filters():
	return frappe.get_all("Role", {"creation": (">", "2020-01-01 00:00:00")}, "disabled", limit=10, run=0)


def bench_get_all_with_many_fields():
	return frappe.get_all(
		"Role",
		{"creation": (">", "2020-01-01 00:00:00")},
		["disabled", "name", "creation", "modified"],
		limit=10,
		run=0,
	)


@lru_cache
def get_all_roles():
	return frappe.get_all("Role", order_by="creation asc", limit=10, pluck="name")
