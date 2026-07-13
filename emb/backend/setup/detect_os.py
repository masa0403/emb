# emb/backend/setup/detect.py
import platform

def detect_os():
    os_name = platform.system().lower()

    if os_name == "linux":
        return "ubuntu"   # まずは ubuntu 固定でOK（後で拡張可能）
    elif os_name == "windows":
        return "windows"
    elif os_name == "darwin":
        return "mac"
    else:
        return "unknown"
