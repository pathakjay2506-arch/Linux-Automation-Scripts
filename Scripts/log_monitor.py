import time

LOG_FILE = "/var/log/syslog"   # Change to any log file
KEYWORDS = ["error", "fail", "critical", "denied"]

def monitor_log(filepath, keywords):
    print(f"👁️  Monitoring: {filepath}")
    print(f"   Watching for: {keywords}\n")
    try:
        with open(filepath, "r") as f:
            f.seek(0, 2)  # Jump to end of file
            while True:
                line = f.readline()
                if line:
                    for keyword in keywords:
                        if keyword.lower() in line.lower():
                            print(f"  🚨 ALERT: {line.strip()}")
                else:
                    time.sleep(0.5)
    except FileNotFoundError:
        print(f"❌ File not found: {filepath}")
    except KeyboardInterrupt:
        print("\n✅ Monitoring stopped.")

if __name__ == "__main__":
    monitor_log(LOG_FILE, KEYWORDS)