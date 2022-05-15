import psutil

# Measure cpu times
def monitor_cpu_times():
    print("\n CPU TIMES")
    cpu_times=psutil.cpu_times()
    user_time=round(cpu_times.user/60)
    system_time=round(cpu_times.system/60)
    idle_time=round(cpu_times.idle/60)
    print(f"time spent on proccess by the User : {user_time} minutes")
    print(f"time spent on proccess by the System : {system_time} minutes")
    print(f"time spent on proccess by Idle : {idle_time} minutes")

# Measure CPU util
def monitor_cpu_util():
    print("\n CPU UTIL")
    print(psutil.cpu_percent())


# Count working CPU cores
def monitor_cpu_cores():
    print("\n CPU CORES")
    print(psutil.cpu_count())

# Measure CPU frequences 
def monitor_cpu_freq():
    print("\n CPU frequences")
    print(f"{psutil.cpu_freq().current} Mhz")


#monitor RAM Usage
def monitor_ram():
    print("\n RAM Usage")
    virtual_memory=psutil.virtual_memory()
    print(f"Total Memory {virtual_memory.total/1073741824} gb")
    print(f"Available Memory {virtual_memory.available/1073741824} gb")
    print(f"used Memory {virtual_memory.used/1073741824} gb")
    print(f"Percentage used {virtual_memory.percent} %")

# Monitor disk partitions
def monitor_disk():
    print("\n DISK PARTITIONS")
    print(psutil.disk_partitions())

# Disk utilization
def monitor_disk_usage():
    print("\n DISK Usage")
    disk_usage=psutil.disk_usage('/')
    print(f"Total Memory {disk_usage.total/1073741824} gb")
    print(f"Available Memory {disk_usage.free/1073741824} gb")
    print(f"used Memory {disk_usage.used/1073741824} gb")
    print(f"Percentage used {disk_usage.percent} %")

# Monitor network requests
def monitor_network():
    print("\n Network requests")
    io_stats=psutil.net_io_counters()
    print(f"total mb sent {io_stats.bytes_sent/1048576} mb")
    print(f"total mb received {io_stats.bytes_recv/1048576} mb")

# Monitor battery usage
def monitor_battrey():
    print("\n MONITORN Battery")
    battery_info=psutil.sensors_battery()
    print(f"Battery percent: {battery_info.percent}")
    print(f"seconds left: {battery_info.secsleft}")

def run_all_checks():
    monitor_cpu_times()
    monitor_cpu_util()
    monitor_cpu_cores()
    monitor_cpu_freq()
    monitor_ram()
    monitor_disk()
    monitor_disk_usage()
    monitor_network()
    monitor_battrey()

run_all_checks()