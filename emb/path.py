from pathlib import Path

PACKAGE = Path(__file__).resolve().parent

ROOT = PACKAGE

BOARDS = PACKAGE / "boards"
FIRMWARE = PACKAGE / "firmware"
SOURCES = PACKAGE / "sources"

BUILD = PACKAGE.parent / "build"
LOGS = PACKAGE.parent / "logs"