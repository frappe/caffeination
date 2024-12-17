from frappe.utils.caching import site_cache


@site_cache
def bench_site_cache_no_arg():
	return 42


@site_cache
def bench_site_cache_many_args(x=4, y="abc", z=1.22):
	return 42


@site_cache(ttl=600)
def bench_site_cache_with_ttl():
	return 42
