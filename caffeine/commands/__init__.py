import subprocess

import click
from frappe.commands import pass_context
from frappe.exceptions import SiteNotSpecifiedError


@click.command(
	"run-microbenchmarks",
	context_settings=dict(
		ignore_unknown_options=True,
	),
	add_help_option=False,
)
@click.argument("benchargs", nargs=-1, type=click.UNPROCESSED)
@pass_context
def run_benchmarks(ctx, benchargs):
	import frappe

	if not ctx.sites:
		raise SiteNotSpecifiedError
	site = ctx.sites[0]
	benchargs = ("--site", site) + benchargs
	frappe.init(site)
	frappe.cache.flushall()

	from caffeine.microbenchmarks import run_benchmarks

	# XXX: We can't invoke it directly pyperf wants to be the entry point
	# Anyway, this shouldn't be a problem. It's no different than shell invoking it.
	subprocess.check_call(["../env/bin/python3", run_benchmarks.__file__, *benchargs])


commands = [
	run_benchmarks,
]
