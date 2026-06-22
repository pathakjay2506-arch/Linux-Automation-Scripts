import os
import shutil

CLEANUP_DIRS = ["/tmp", os.path.expanduser("~/.cache")]

def cleanup(directories):
    total_freed = 0
    print("\n🧹 Starting Disk Cleanup...\n")

    for directory in directories:
        if not os.path.exists(directory):
            print(f"  Skipping {directory} (not found)")
            continue
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            try:
                size = os.path.getsize(item_path)
                if os.path.isfile(item_path):
                    os.remove(item_path)
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)
                total_freed += size
                print(f"  ✅ Deleted: {item_path}")
            except Exception as e:
                print(f"  ❌ Skipped: {item_path} ({e})")

    print(f"\n🎉 Done! Freed up: {total_freed / (1024*1024):.2f} MB\n")

if __name__ == "__main__":
    cleanup(CLEANUP_DIRS)