import frappe


def bench_qb_select_star():
	table = frappe.qb.DocType("Role")
	return frappe.qb.from_(table).select("*").limit(20).run(run=0)


def bench_qb_select_star_multiple_fields():
	table = frappe.qb.DocType("Role")
	return frappe.qb.from_(table).select(table.name, table.creation, table.modified).limit(20).run(run=0)


def bench_qb_get_query():
	return frappe.qb.get_query(
		"Role",
		filters={"creation": (">", "2020-01-01 00:00:00")},
		fields="disabled",
		limit=10,
		order_by="creation asc",
	).run(run=0)


def bench_qb_get_query_multiple_fields():
	return frappe.qb.get_query(
		"Role",
		filters={"creation": (">", "2020-01-01 00:00:00")},
		fields=["disabled", "name", "creation", "modified"],
		limit=10,
		order_by="creation asc",
	).run(run=0)


def bench_qb_simple_get_query():
	return frappe.qb.get_query(
		"Role",
		filters={"name": "Guest"},
		fields="*",
		limit=1,
		order_by="creation asc",
	).run(run=0)
