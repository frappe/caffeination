### Caffeination

Frappes are usually not caffeinated enough, we want a lot of caffeine in ours.

### Goal

This project has only one goal: **Speedup Frappe ecosystem by approximately by 2x.**

Approximately, this boils down to:
- Setup a good benchmark suite consisting benchmarks ranging from microbenchmarks to realistic traces.
- Remove unnecessary overheads wherever possible. Every 0.1% on critical path counts.
- Make deployments resource efficient by tuning various knobs.


### Terminology

Speedup is always defined as follows:
- throughput: after/before. E.g. 20rps / 10rps = 2x
- latency: before/after. E.g. 20ms / 10ms = 2x

Slowdown can be reported as follows:
- latency: before/after. E.g. 5ms / 10ms = 0.5x a.k.a "2x slowdown"

Efficiency improvements are defined similarly:
- memory usage improvement w/ same performance (Pss): before/after. E.g. 200MB/100MB = 2x

### Contributing

This repo is not accepting any external contributions at present.

### License

MIT
