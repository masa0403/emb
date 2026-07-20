import json


REQUEST_JSON = "requests/test_request.json"

HARDWARE_JSON = "target_mcu/attiny202/hardware.json"

EXPECTED_JSON = "logs/expected.json"



def load_json(path):

    with open(path,"r") as f:
        return json.load(f)



def main():

    request = load_json(REQUEST_JSON)

    hardware = load_json(HARDWARE_JSON)


    mcu_name = hardware["target_mcu"]["name"]


    events=[]


    for e in request["expected_events"]:

        events.append(
            {
                "pin":
                    mcu_name + "." + e["pin"],

                "type":
                    e["type"]
            }
        )


    expected={

        "events":events

    }


    with open(EXPECTED_JSON,"w") as f:

        json.dump(
            expected,
            f,
            indent=4
        )


    print("expected.json generated")



if __name__=="__main__":

    main()