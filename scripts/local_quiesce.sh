#!/bin/bash

set -x
set -e

# This script is not general purpose, modify for your needs
# All the changes are temporary and go away on boot
# ref: https://llvm.org/docs/Benchmarking.html

# Set performance governor

for i in 0 2 4 6 8 10 12 14
do
  echo "performance" | sudo tee /sys/devices/system/cpu/cpu$i/cpufreq/scaling_governor
done


# Remove effects of SMT
echo "off" | sudo tee /sys/devices/system/cpu/smt/control

# Alt: disabling 1 thread in each core
# I have 16 threads and topology is 0-1, 2-3, 4-5...
# So I disable each odd numbered thread.
# for cpu_no in 1 3 5 7 9 11 13 15
# do
#   echo 0 | sudo tee /sys/devices/system/cpu/cpu$cpu_no/online
# done


# Disable turbo boosting
# I use pstate driver and this is "guaranteed" performance state ~ 2.7GHz, setting it to max prevents boosting.
# There are probaly better way to do this.
for cpu_no in 0 2 4 6 8 10 12 14
do
  echo 2700000 | sudo tee /sys/devices/system/cpu/cpufreq/policy$cpu_no/scaling_max_freq
done

# Disable ASLR
echo 0 | sudo tee /proc/sys/kernel/randomize_va_space
