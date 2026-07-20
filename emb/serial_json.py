import json
import re


def save_latest_json(logs, filename="logs/latest.json"):

    events = []
    tester_log = []
    system = []


    for line in logs:

        line = line.strip()


        if line.startswith("#SYS"):
            system.append(line)
            continue


        if line.startswith("#TEST"):
            tester_log.append(line)
            continue


        match = re.match(
            r"(\d+),(\d+),([^,]+),(RISE|FALL)",
            line
        )


        if match:

            events.append(
                {
                    "seq": int(match.group(1)),
                    "time_us": int(match.group(2)),
                    "pin": match.group(3),
                    "type": match.group(4)
                }
            )


    data = {

        "version":1,

        "events":events,

        "tester_log":tester_log,

        "system":system

    }


    with open(filename,"w",encoding="utf-8") as f:

        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )


    print("JSON saved:",filename)