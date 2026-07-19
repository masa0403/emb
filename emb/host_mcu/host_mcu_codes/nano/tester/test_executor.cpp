#include "test_executor.h"

#include "test_plan.h"

TestExecutor testExecutor;

void TestExecutor::begin()
{
    currentCommand = 0;

    waitingDelay = false;

    pinMode(7, OUTPUT);
    pinMode(8, OUTPUT);

    digitalWrite(7, LOW);
    digitalWrite(8, LOW);
}

void TestExecutor::update()
{
    if(waitingDelay)
    {
        if(millis() < waitUntil)
        {
            return;
        }

        waitingDelay = false;
    }
    if(waitingPin)
    {
        const TestCommand& cmd = TEST_PLAN[currentCommand];

        bool state = digitalRead(cmd.pin);

        if(cmd.type == CMD_WAIT_HIGH)
        {
            if(state == LOW)
                return;
        }

        if(cmd.type == CMD_WAIT_LOW)
        {
            if(state == HIGH)
                return;
        }

        waitingPin = false;

        currentCommand++;
    }

    const TestCommand& cmd = TEST_PLAN[currentCommand];

    switch(cmd.type)
    {
        case CMD_DELAY:

            Serial.print("#TEST,");

            Serial.print(currentCommand);

            Serial.print(",DELAY,");

            Serial.println(cmd.value);

            waitUntil = millis()+cmd.value;

            waitingDelay = true;

            currentCommand++;

            break;

        case CMD_PIN_HIGH:

            Serial.print("#TEST,");

            Serial.print(currentCommand);

            Serial.print(",PIN_HIGH,D");

            Serial.println(cmd.pin);

            digitalWrite(cmd.pin,HIGH);

            currentCommand++;

            break;

        case CMD_PIN_LOW:

            Serial.print("#TEST,");
            Serial.print(currentCommand);
            Serial.print(",PIN_LOW,D");
            Serial.println(cmd.pin);

            digitalWrite(cmd.pin,LOW);

            currentCommand++;

            break;

        case CMD_WAIT_HIGH:

            Serial.print("#TEST,");

            Serial.print(currentCommand);

            Serial.print(",WAIT_HIGH,D");

            Serial.println(cmd.pin);

            waitingPin = true;

            break;

        case CMD_WAIT_LOW:

            Serial.print("#TEST,");

            Serial.print(currentCommand);

            Serial.print(",WAIT_LOW,D");

            Serial.println(cmd.pin);

            waitingPin = true;

            break;

        case CMD_END:

            return;
    }
}

