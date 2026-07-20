from pathlib import Path
import subprocess

ARDUINO_CLI = "./bin/bin/arduino-cli"

def run(cmd):

    print(">>", " ".join(cmd))

    subprocess.check_call(cmd)



# ----------------------------------------
# Step 1
# Generate test_plan.cpp
# ----------------------------------------

print("[1] Generate Nano TestPlan")

run([
    "python3",
    "generate_nano_code.py"
])



# ----------------------------------------
# Step 2
# Compile Nano Tester
# ----------------------------------------

print("[2] Compile Nano Tester")


nano_sketch = (
    "host_mcu/host_mcu_codes/nano/tester/tester.ino"
)


run([
    ARDUINO_CLI,
    "compile",
    "--fqbn",
    "arduino:avr:nano",
    nano_sketch
])



# ----------------------------------------
# Step 3
# Upload Nano Tester
# ----------------------------------------

print("[3] Upload Nano Tester")


# 今は固定
# 後でdetect_nano_port()へ変更

port = "/dev/ttyUSB0"


run([
    ARDUINO_CLI,
    "upload",
    "-p",
    port,
    "--fqbn",
    "arduino:avr:nano",
    nano_sketch
])


print()
print("=== Nano Test Ready ===")