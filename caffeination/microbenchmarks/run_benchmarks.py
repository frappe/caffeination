#!/bin/env python3

import inspect
import os
from types import FunctionType

import frappe
import pyperf

from caffeination.microbenchmarks import bench_database, bench_orm, bench_redis

BENCHMARK_PREFIX = "bench_"
BENCHMARK_SITE = os.environ.get("FRAPPE_BENCHMARK_SITE") or "bench.localhost"


def run_microbenchmarks():
	benchmarks = discover_benchmarks()

	frappe.init(BENCHMARK_SITE)
	frappe.connect()

	runner = pyperf.Runner()
	for name, func in benchmarks:
		runner.bench_func(name, func)

	frappe.destroy()


def discover_benchmarks():
	benchmark_modules = [
		bench_orm,
		bench_database,
		bench_redis,
	]

	benchmarks = []
	for module in benchmark_modules:
		module_name = module.__name__.split(".")[-1]
		for fn_name, fn in inspect.getmembers(module, predicate=lambda x: isinstance(x, FunctionType)):
			if fn_name.startswith(BENCHMARK_PREFIX):
				unique_name = f"{module_name}_{fn.__name__.removeprefix(BENCHMARK_PREFIX)}"
				benchmarks.append((unique_name, fn))

	return sorted(benchmarks, key=lambda x: x[0])


if __name__ == "__main__":
	run_microbenchmarks()
