import json


HARDWARE_JSON = "target_mcu/attiny202/hardware.json"
LATEST_JSON = "logs/latest.json"
EXPECTED_JSON = "logs/expected.json"


def load_json(path):

    with open(path, "r") as f:
        return json.load(f)



# hardware.jsonから
# ATtiny202.PA2 → latest.json形式
# の対応表を作る
def create_pin_map(hardware):

    monitor_pins = hardware["host_mcu"]["monitor_pins"]

    pin_map = {}

    for host_pin, target_pin in monitor_pins.items():

        # target.PA2
        target_pin = target_pin.replace(
            "target.",
            ""
        )

        pin_map[host_pin] = (
            hardware["target_mcu"]["name"]
            + "."
            + target_pin
        )

    return pin_map



def normalize_event(event):

    return {
        "pin": event["pin"],
        "type": event["type"]
    }



def compare():

    hardware = load_json(
        HARDWARE_JSON
    )

    latest = load_json(
        LATEST_JSON
    )

    expected = load_json(
        EXPECTED_JSON
    )


    # 現在はlatest.jsonが
    # ATtiny202.PA2形式なので
    # hardware変換は不要
    actual_events=[]


    for event in latest["events"]:

        actual_events.append(
            normalize_event(event)
        )


    missing=[]


    for event in expected["events"]:

        if event not in actual_events:

            missing.append(event)



    if missing:

        result={
            "status":"FAIL",
            "expected_count":len(expected["events"]),
            "actual_count":len(actual_events),
            "missing":missing
        }

    else:

        result={
            "status":"PASS",
            "expected_count":len(expected["events"]),
            "actual_count":len(actual_events),
            "missing":[]
        }


    print(
        json.dumps(
            result,
            indent=4
        )
    )



if __name__=="__main__":

    compare()