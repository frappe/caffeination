#!/bin/env python3

import inspect
from types import FunctionType

import frappe
import pyperf
from frappe.utils import cstr

from caffeination.microbenchmarks import (
	bench_background_jobs,
	bench_database,
	bench_orm,
	bench_redis,
	bench_web_requests,
)

BENCHMARK_PREFIX = "bench_"


def run_microbenchmarks():
	def update_cmd_line(cmd, args):
		# Pass our added arguments to workers
		cmd.extend(["--site", args.site])
		cmd.extend(["--filter", args.benchmark_filter])

	runner = pyperf.Runner(add_cmdline_args=update_cmd_line)

	runner.argparser.add_argument(
		"--filter",
		dest="benchmark_filter",
		help="Apply a filter to selectively run benchmarks. This is a substring filter.",
	)
	runner.argparser.add_argument(
		"--site", dest="site", help="Frappe site to use for benchmark", required=True
	)

	args = runner.argparser.parse_args()
	benchmarks = discover_benchmarks(args.benchmark_filter)
	setup(args.site)
	for name, func in benchmarks:
		runner.bench_func(name, func)
	teardown(args.site)


def setup(site):
	frappe.init(site)
	frappe.connect()


def teardown(site):
	frappe.destroy()


def discover_benchmarks(benchmark_filter=None):
	benchmark_filter = cstr(benchmark_filter)
	benchmark_modules = [bench_orm, bench_database, bench_redis, bench_background_jobs, bench_web_requests]

	benchmarks = []
	for module in benchmark_modules:
		module_name = module.__name__.split(".")[-1]
		for fn_name, fn in inspect.getmembers(module, predicate=lambda x: isinstance(x, FunctionType)):
			if fn_name.startswith(BENCHMARK_PREFIX):
				unique_name = f"{module_name}_{fn.__name__}"
				if benchmark_filter in unique_name:
					benchmarks.append((unique_name, fn))

	return sorted(benchmarks, key=lambda x: x[0])


if __name__ == "__main__":
	run_microbenchmarks()
