import frappe
from frappe.utils import execute_in_shell


# def bench_bg_job_overheads():
# 	for _ in range(10):
# 		frappe.enqueue(frappe.ping)
# 	# XXX: We are counting startup costs into this.
# 	_, stderr = execute_in_shell("bench worker --burst", check_exit_code=True)
# 	assert b"Job OK" in stderr
