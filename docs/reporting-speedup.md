# Reporting Speedup

Speedups should **always** be reported as a ratio. Here is the basic formula:

- Latency speedup: latency **before** / latency **after**. E.g. 10ms / 5ms = 2x.
- Throughput speedup: throughput **after** / throughput **before**. E.g. 150 rps / 100 rps = 1.5x

Slowdown is just the inverse of speedup.

## Rationale

- Most of the academic literature follows this convention.
- Ratios are simpler to understand: “It is now 1.5x faster” doesn't have different interpretations. (?)
- It is unlikely to cause confusion that is inherent in percentages.
    - E.g. "50% improvement" can mean 10ms → 5ms (2x speedup) OR it can mean 15ms → 10ms. (1.5x speedup)
- \>= 2x improvements are even more confusing to represent with percentages. 100% means 2x. 200% means 3x.
