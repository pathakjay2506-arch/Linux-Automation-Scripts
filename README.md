# 🐧 Linux Automation Scripts

A collection of Python and Bash scripts to automate common Linux sysadmin tasks.

## 📋 Scripts Included

| Script | Description |
|--------|-------------|
| `system_health.py` | Reports CPU, RAM, Disk usage with alerts |
| `disk_cleanup.py` | Cleans temp and cache files automatically |
| `log_monitor.py` | Watches log files for errors in real-time |
| `user_manager.sh` | Interactive tool to add/remove Linux users |

## 🚀 How to Run

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/linux-automation-scripts.git
cd linux-automation-scripts

# Install dependencies
pip install -r requirements.txt

# Run any script
python3 scripts/system_health.py
python3 scripts/disk_cleanup.py
bash scripts/user_manager.sh
```

## 🛠️ Tech Stack
- Python 3
- Bash
- psutil library
- Linux (Ubuntu/Debian)
