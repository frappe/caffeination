import time

from frappe.utils.caching import request_cache, site_cache


@site_cache
def bench_site_cache_no_arg():
	time.sleep(0.1)
	return 42


@site_cache
def bench_site_cache_many_args(x=4, y="abc", z=1.22):
	time.sleep(0.1)
	return 42


@site_cache(ttl=600)
def bench_site_cache_with_ttl():
	time.sleep(0.1)
	return 42


@request_cache
def bench_request_cache_many_args(x=4, y="abc", z=1.22):
	time.sleep(0.1)
	return 42
