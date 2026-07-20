import json
from pathlib import Path


RESULT_JSON = Path("logs/result.json")

TEST_REQUEST_JSON = Path(
    "requests/test_request.json"
)

TEST_PLAN_JSON = Path(
    "logs/nano_test_plan.json"
)

HARDWARE_JSON = Path(
    "target_mcu/attiny202/hardware.json"
)

OUTPUT_JSON = Path(
    "logs/ai_feedback.json"
)

def load_json(path):

    with open(path, "r") as f:
        return json.load(f)



def generate_feedback(
    result,
    test_request,
    test_plan,
    hardware
):

    feedback = {
        "version":1,

        "role":"embedded_debug_ai",

        "context":{

            "target_mcu":
            hardware["target_mcu"]["name"],

            "host_mcu":
            hardware["host_mcu"]["name"],

            "hardware":
            hardware,

            "test_request":
            test_request,

            "test_plan":
            test_plan

        },

        "evaluation": {
            "status": result["status"],
            "expected_events": result["expected_count"],
            "actual_events": result["actual_count"]
        },

        "failure_analysis": {

            "missing_events": result.get(
                "missing",
                []
            ),

            "unexpected_events": result.get(
                "extra",
                []
            )

        },

        "instruction": ""
    }


    if result["status"] == "PASS":

        feedback["instruction"] = (
            "Test passed. "
            "No hardware correction is required."
        )

    else:

        feedback["instruction"] = (
            "Analyze missing hardware events. "
            "Determine whether firmware, timing, "
            "pin assignment, or test plan should be modified."
        )


    return feedback



def main():

    result = load_json(
        RESULT_JSON
    )

    test_request = load_json(
        TEST_REQUEST_JSON
    )

    test_plan = load_json(
        TEST_PLAN_JSON
    )

    hardware = load_json(
        HARDWARE_JSON
    )


    feedback = generate_feedback(
        result,
        test_request,
        test_plan,
        hardware
    )

    with open(
        OUTPUT_JSON,
        "w"
    ) as f:

        json.dump(
            feedback,
            f,
            indent=4
        )


    print("ai_feedback.json generated")



if __name__ == "__main__":
    main()