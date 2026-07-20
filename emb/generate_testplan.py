import json


PLAN_JSON = "test_plan.json"

HARDWARE_JSON = "target_mcu/attiny202/hardware.json"

OUTPUT_JSON = "logs/nano_test_plan.json"



def load(path):

    with open(path,"r") as f:
        return json.load(f)



def create_pin_map(hardware):

    pins = hardware["target_mcu"]["pins"]

    return pins



def main():

    plan = load(PLAN_JSON)

    hardware = load(HARDWARE_JSON)


    pin_map = create_pin_map(hardware)


    commands=[]


    for cmd in plan["commands"]:

        new_cmd = cmd.copy()


        if "pin" in cmd:

            pin = cmd["pin"]

            new_cmd["pin"] = pin_map[pin]


        commands.append(new_cmd)



    output = {

        "version":1,

        "commands":commands

    }



    with open(OUTPUT_JSON,"w") as f:

        json.dump(
            output,
            f,
            indent=4
        )


    print("nano_test_plan.json generated")



if __name__=="__main__":

    main()