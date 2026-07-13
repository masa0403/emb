import sys

from emb.commands.flash import main as flash_command
from emb.commands.setup import main as setup_command

SUPPORTED_BOARDS = {
    "attiny202",
}

def main():

    if len(sys.argv) < 2:
        print(
            "Usage:\n"
            "\n"
            "1. Setup\n"
            "   emb setup <target_mcu_name>\n"
            "\n"
            "2. Flash & Log\n"
            "   emb <target_mcu_name> <source_code> <port>\n"
            "\n"
            "Note 😉\n"
            "   Place your source code under:\n"
            "   emb-loop/emb/sources/<target_mcu_name>/\n"
            "\n"
            "Example:\n"
            "   emb-loop/emb/sources/attiny202/blink.c\n"
        )

        return

    first = sys.argv[1]

    # setupだけは特別扱い
    if first == "setup":

        setup_command(sys.argv[2:])
        return

    # ボード名なら自動でFlashパイプラインを開始
    if first in SUPPORTED_BOARDS:

        flash_command(sys.argv[1:])
        return

    print(f"Unknown board or command: {first}")


if __name__ == "__main__":
    main()