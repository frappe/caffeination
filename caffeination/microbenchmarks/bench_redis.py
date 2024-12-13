from functools import lru_cache

import frappe


def bench_make_key():
	keys = []
	for dt in get_all_doctypes():
		keys.append(frappe.cache.make_key(dt))
	return keys


def bench_set_value():
	for dt in get_all_doctypes():
		key = f"_test_set_value:{dt}"
		frappe.cache.set_value(key, cached_get_doc(dt), expires_in_sec=30)
		assert frappe.cache.exists(key)
		assert frappe.cache.get_value(key).name == dt
	frappe.local.cache.clear()


@lru_cache
def get_all_doctypes():
	return frappe.get_all("DocType", order_by="creation asc", limit=100, pluck="name")


@lru_cache
def cached_get_doc(doctype):
	return frappe.get_doc("DocType", doctype)
