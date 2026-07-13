# emb/commands/setup.py

import sys
from emb.backend.setup.ubuntu import check_ubuntu_avr_toolchain
from emb.backend.avr.toolchain import resolve_avr_toolchain
from emb.backend.avr.flash import flash_hex
from emb.backend.avr.compile import compile_source
from emb.backend.setup.detect import detect_os


def main(args):
    if len(args) == 0:
        print("Usage: emb setup <target>")
        return

    target = args[0].lower()

    # OS 自動判定
    os_name = detect_os()

    # OS ごとに check 関数をロード
    if os_name == "ubuntu":
        from emb.backend.setup.ubuntu import check_ubuntu_avr_toolchain
    else:
        print("Unsupported OS")
        return

    if target == "attiny202":
        print(f"Detected OS: {os_name}")
        print("Checking environment for ATtiny202...")
        check_ubuntu_avr_toolchain()
        print("Setting up environment for ATtiny202...")
        resolve_avr_toolchain("attiny202")
        print("ATtiny202 environment is ready.")
        return

    else:
        print(f"Unknown setup target: {target}")
        return
