import subprocess
import time

while True:
    print("[WATCHDOG] Starting main.py")
    p = subprocess.Popen(["python", "main.py"])
    p.wait()
    print("[WATCHDOG] Crashed, restarting in 5s")
    time.sleep(5)
