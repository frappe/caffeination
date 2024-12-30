#!/bin/bash

set -x
set -e

# Switch back performance governor
for i in 0 1 2 3 4 5 6 7
do
  echo "powersave" | sudo tee /sys/devices/system/cpu/cpu$i/cpufreq/scaling_governor
done


# Enable SMT
echo "on" | sudo tee /sys/devices/system/cpu/smt/control


# Enable max turbo frequencies
for cpu_no in 0 1 2 3 4 5 6 7
do
  echo 5389000 | sudo tee /sys/devices/system/cpu/cpufreq/policy$cpu_no/scaling_max_freq
done

# Enable ASLR
echo 2 | sudo tee /proc/sys/kernel/randomize_va_space
