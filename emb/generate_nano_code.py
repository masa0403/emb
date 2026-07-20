import json


INPUT = "logs/nano_test_plan.json"

OUTPUT = (
    "host_mcu/host_mcu_codes/nano/tester/test_plan.cpp"
)


def convert_command(cmd):

    name = cmd["cmd"]

    if name == "DELAY":

        return (
            f"    {{CMD_DELAY,0,{cmd['value']}}}"
        )


    if name == "PIN_HIGH":

        pin = cmd["pin"].replace("D","")

        return (
            f"    {{CMD_PIN_HIGH,{pin},0}}"
        )


    if name == "PIN_LOW":

        pin = cmd["pin"].replace("D","")

        return (
            f"    {{CMD_PIN_LOW,{pin},0}}"
        )


    if name == "END":

        return (
            "    {CMD_END,0,0}"
        )


    raise Exception(
        f"Unknown command {name}"
    )



def main():

    with open(INPUT) as f:
        data=json.load(f)


    lines=[]

    lines.append(
        '#include "test_plan.h"\n'
    )

    lines.append(
        "const TestCommand TEST_PLAN[] =\n"
    )

    lines.append(
        "{\n"
    )


    for cmd in data["commands"]:

        lines.append(
            convert_command(cmd)
            + ",\n\n"
        )


    lines.append(
        "};\n"
    )


    with open(OUTPUT,"w") as f:

        f.write(
            "".join(lines)
        )


    print(
        "test_plan.cpp generated"
    )



if __name__=="__main__":

    main()