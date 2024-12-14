from functools import lru_cache

import frappe
from frappe.app import application as _trigger_imports
from frappe.utils import get_test_client


def bench_request_overheads():
	client = get_test_client()
	for _ in range(100):
		resp = client.get("/api/method/ping", headers={"X-Frappe-Site-Name": get_site()})
		assert resp.status_code == 200


@lru_cache
def get_site():
	return frappe.local.site
