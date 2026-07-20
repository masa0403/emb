import re

EVENT_PATTERN = re.compile(
    r"(\d+),(\d+),([^,]+),(RISE|FALL)"
)

TEST_PATTERN = re.compile(
    r"#TEST,(.+)"
)


def parse_serial_log(lines):
    result = {
        "events": [],
        "tester_log": [],
        "system": []
    }

    for line in lines:

        line = line.strip()

        if not line:
            continue

        if line.startswith("#SYS"):
            result["system"].append(line)
            continue

        if line.startswith("#TEST"):
            result["tester_log"].append(line)
            continue

        m = EVENT_PATTERN.match(line)

        if m:

            result["events"].append({
                "seq": int(m.group(1)),
                "time_us": int(m.group(2)),
                "pin": m.group(3),
                "type": m.group(4)
            })

    return result