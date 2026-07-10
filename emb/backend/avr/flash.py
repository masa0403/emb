from pathlib import Path
import subprocess
import sys
import os
import time
from pathlib import Path
from pin_logger import capture_pin_log

# -----------------------------
# 引数チェック
# -----------------------------
if len(sys.argv) != 3:
    print("使い方:")
    print("    python chatgpt_writer.py <source.c> <COMポート>")
    print("例:")
    print("    python chatgpt_writer.py test.c COM3")
    sys.exit(1)

SRC = sys.argv[1]
COM_PORT = sys.argv[2]

# -----------------------------
# ログファイル作成
# -----------------------------
# logs ディレクトリ
BASE = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(BASE, "logs")
os.makedirs(LOG_DIR, exist_ok=True)

# behave_logs ディレクトリ
BEHAVE_DIR = os.path.join(BASE, "behave_logs")
os.makedirs(BEHAVE_DIR, exist_ok=True)

def create_log_file():
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    nums = []
    for f in log_dir.glob("*.txt"):
        try:
            nums.append(int(f.stem))
        except ValueError:
            pass

    next_num = max(nums, default=0) + 1
    return log_dir / f"{next_num:04d}.txt"

def write_behavior_log(content):
    existing = [f for f in os.listdir(BEHAVE_DIR) if f.startswith("behave_") and f.endswith(".txt")]
    nums = []
    for f in existing:
        try:
            n = int(f[7:10])
            nums.append(n)
        except:
            pass
    next_num = max(nums) + 1 if nums else 1
    path = os.path.join(BEHAVE_DIR, f"behave_{next_num:03d}.txt")

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[INFO] Behavior Log saved: {path}")


# -----------------------------
# ファイル名生成
# -----------------------------
base = Path(SRC).stem

ELF = base + ".elf"
HEX = base + ".hex"

MCU = "attiny202"
BAUD = "115200"

# -----------------------------
# コンパイル
# -----------------------------
print("Compiling...")

subprocess.check_call([
    "avr-gcc",
    "-mmcu=" + MCU,
    "-Os",
    "-DF_CPU=5000000UL",
    SRC,
    "-o",
    ELF
])

print("Creating HEX...")

subprocess.check_call([
    "avr-objcopy",
    "-O",
    "ihex",
    ELF,
    HEX
])

print("Compile OK")

# -----------------------------
# 書き込み
# -----------------------------
print("Writing...")

log_file = create_log_file()

result = subprocess.run(
    [
        "avrdude",
        "-v",
        "-p", MCU,
        "-c", "jtag2updi",
        "-P", COM_PORT,
        "-b", BAUD,
        "-U", f"flash:w:{HEX}:i"
    ],
    capture_output=True,
    text=True
)

# コンソールへ表示
print(result.stdout)
print(result.stderr)

# ログ保存
with open(log_file, "w", encoding="utf-8") as f:
    f.write(result.stdout)
    f.write(result.stderr)

if result.returncode != 0:
    raise subprocess.CalledProcessError(result.returncode, result.args)

print(f"Log saved : {log_file}")
print("Done!")


# DUTのピン状態を監視する
print("[INFO] Capturing pin behavior...")
time.sleep(5.0)

try:
    log_data = capture_pin_log(port="COM3", baud=115200, duration=50)
except Exception as e:
    print("[ERROR] pin_logger failed:", e)
    write_behavior_log(f"[ERROR] pin_logger failed: {e}\n")
    sys.exit(1)

# ★ ピン挙動ログは behave_logs/ に保存
behavior_text = "\n".join(log_data)
write_behavior_log(behavior_text)