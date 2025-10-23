import time
import os
import platform
from datetime import datetime as dt
import ctypes  # for admin check on Windows


def get_hosts_path():
    system = platform.system()
    if system == "Windows":
        return os.path.join(os.environ.get("SystemRoot", "C:\\Windows"),
                            "System32", "drivers", "etc", "hosts")
    elif system in ("Linux", "Darwin"):
        return "/etc/hosts"
    else:
        raise OSError(f"Unsupported OS: {system}")

def is_admin():
    if platform.system() == "Windows":
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
    else:
        # On Linux/macOS, assume root user has UID 0
        return os.geteuid() == 0


def block_websites(hosts_path, websites, redirect):
    with open(hosts_path, "r+") as file:
        content = file.read()
        for website in websites:
            if website not in content:
                file.write(f"{redirect} {website}\n")
                print(f"[BLOCKED] {website}")


def unblock_websites(hosts_path, websites):
    with open(hosts_path, "r+") as file:
        content = file.readlines()
        file.seek(0)
        for line in content:
            if not any(website in line for website in websites):
                file.write(line)
        file.truncate()
    print("[UNBLOCKED] All websites removed from block list")

def main():
    if not is_admin():
        print("⚠️ Please run this script as Administrator/root!")
        return

    hosts_path = get_hosts_path()
    redirect = "127.0.0.1"
    website_list = [
        "www.facebook.com",
        "facebook.com",
        "dub119.mail.live.com",
        "www.dub119.mail.live.com",
        "www.gmail.com",
        "gmail.com",
    ]

    work_start = 10 # 10 AM
    work_end = 16 # 4 PM

    print("Website blocker started... Press Ctrl+C to exit.")
    
    try:
        while True:
            now = dt.now()
            if work_start <= now.hour < work_end:
                print(f"{now.strftime('%H:%M:%S')} - Working hours...")
                block_websites(hosts_path, website_list, redirect)
            else:
                print(f"{now.strftime('%H:%M:%S')} - Fun hours...")
                unblock_websites(hosts_path, website_list)
            time.sleep(30)  # check every 30 seconds
    except KeyboardInterrupt:
        print("\nExiting... Goodbye!")

if __name__ == "__main__":
    main()
