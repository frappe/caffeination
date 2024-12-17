import time

import frappe
from frappe.utils.caching import redis_cache, request_cache, site_cache


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


def bench_redis_cache_deco_with_local_cache():
	for i in range(100):
		cache_in_redis(i)


def bench_redis_cache_deco_without_local_cache():
	for i in range(100):
		cache_in_redis(i)
	frappe.local.cache.clear()


@redis_cache
def cache_in_redis(num):
	time.sleep(0.001)
	return num
