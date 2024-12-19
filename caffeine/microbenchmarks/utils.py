from dataclasses import dataclass
from typing import Any


@dataclass
class NanoBenchmark:
	statement: str
	setup: str = "pass"
	teardown: str = "pass"
	globals: dict[str, Any] | None = None
