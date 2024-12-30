#!/bin/bash

set -x
set -e

# This script is not general purpose, modify for your needs
# All the changes are temporary and go away on boot
# ref: https://llvm.org/docs/Benchmarking.html

# Set performance governor
for i in 0 1 2 3 4 5 6 7
do
  echo "performance" | sudo tee /sys/devices/system/cpu/cpu$i/cpufreq/scaling_governor
done


# Remove effects of SMT
echo "off" | sudo tee /sys/devices/system/cpu/smt/control

# Disable turbo boosting
for cpu_no in 0 1 2 3 4 5 6 7
do
  echo 3000000 | sudo tee /sys/devices/system/cpu/cpufreq/policy$cpu_no/scaling_max_freq
done

# Disable ASLR
echo 0 | sudo tee /proc/sys/kernel/randomize_va_space
