#ifndef TEST_PLAN_H
#define TEST_PLAN_H

#include <Arduino.h>

enum TestCommandType
{
    CMD_DELAY,
    CMD_PIN_HIGH,
    CMD_PIN_LOW,
    CMD_WAIT_HIGH,
    CMD_WAIT_LOW,
    CMD_END
};

struct TestCommand
{
    TestCommandType type;
    uint8_t pin;
    uint32_t value;
};

extern const TestCommand TEST_PLAN[];

#endif