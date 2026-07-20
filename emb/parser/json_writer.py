import json


def write_latest_json(parsed, path):

    latest = {

        "version": 1,

        "status": "unknown",

        "summary": {

            "event_count": len(parsed["events"])

        },

        "events": parsed["events"],

        "tester_log": parsed["tester_log"],

        "system": parsed["system"]
    }

    with open(path, "w", encoding="utf-8") as f:

        json.dump(
            latest,
            f,
            indent=4,
            ensure_ascii=False
        )