import psutil
import datetime

def get_system_health():
    print("=" * 45)
    print(f"  System Health Report")
    print(f"  {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 45)

    # CPU
    cpu = psutil.cpu_percent(interval=1)
    print(f"  CPU Usage     : {cpu}%  {'⚠️  HIGH' if cpu > 80 else '✅ OK'}")

    # RAM
    ram = psutil.virtual_memory()
    print(f"  RAM Usage     : {ram.percent}%  {'⚠️  HIGH' if ram.percent > 80 else '✅ OK'}")

    # Disk
    disk = psutil.disk_usage('/')
    print(f"  Disk Usage    : {disk.percent}%  {'⚠️  HIGH' if disk.percent > 80 else '✅ OK'}")

    # Uptime
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    uptime = datetime.datetime.now() - boot_time
    print(f"  System Uptime : {str(uptime).split('.')[0]}")
    print("=" * 45)

if __name__ == "__main__":
    get_system_health()