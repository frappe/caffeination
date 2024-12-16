from functools import lru_cache

import frappe


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
