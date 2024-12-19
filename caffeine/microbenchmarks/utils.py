from dataclasses import dataclass
from typing import Any


@dataclass
class NanoBenchmark:
	"""This class can be used to represent benchmarks that measure sub-milisecond operations.

	These measurement are affected by function call overhead, so instead directly executing the
	statement avoids it."""

	statement: str
	setup: str = "pass"
	teardown: str = "pass"
	globals: dict[str, Any] | None = None
