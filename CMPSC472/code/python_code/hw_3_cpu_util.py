import psutil

"""
Explanation of Results

- CPU: time spent in different modes, core count, usage stats, frequency, and utilization percentage.
- Memory: virtual memory stats and swap memory usage (memory available for transfer to/from RAM and SSD).
- Disk: disk space usage on partitions and disk I/O operations count.
- Network (I/O): network transmission statistics such as bytes sent and received.
- Battery: current battery level and status, if applicable.

"""

# CPU Data
print("\n\t------------------------------------------------------ CPU ------------------------------------------------------")
print("CPU Times:", str(psutil.cpu_times()))  # CPU time
print("CPU Count:", str(psutil.cpu_count()))  # Number of CPUs
print("CPU Stats:", str(psutil.cpu_stats()))  # Usage stats (context switches, interrupts, soft interrupts, syscalls)
print("CPU Frequency:", str(psutil.cpu_freq()))  # Core frequency
print("CPU Percent:", str(psutil.cpu_percent(interval=1, percpu=True)))  # Each core % utilization

# Memory
print("\n\t------------------------------------------------------ Memory ------------------------------------------------------")
print("Total Memory:", str(psutil.virtual_memory()))  # Total memory
print("Swap Memory:", str(psutil.swap_memory()))  # Swap memory - hard drive space used when RAM runs out

# Disk Stats
print("\n\t------------------------------------------------------ Disk ------------------------------------------------------")
print("Disk Usage:", str(psutil.disk_usage('/')))  # Total partition count
print("Disk IO Counters:", str(psutil.disk_io_counters()))  # Read/write to disk operations

# Network
print("\n\t------------------------------------------------------ I/O (Network)  ------------------------------------------------------")
print("Network IO Counters:", str(psutil.net_io_counters()))  # Network transmission stats

# Battery
print("\n\t------------------------------------------------------ Battery ------------------------------------------------------")
print("Battery Status:", str(list(psutil.sensors_battery())))  # Battery remaining