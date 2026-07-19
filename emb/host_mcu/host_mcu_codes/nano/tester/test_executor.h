#ifndef TEST_EXECUTOR_H
#define TEST_EXECUTOR_H

#include <Arduino.h>

class TestExecutor
{
public:

    void begin();

    void update();

private:

    uint16_t currentCommand = 0;

    uint32_t waitUntil = 0;

    bool waitingDelay = false;

    bool waitingPin = false;
};

extern TestExecutor testExecutor;
#endif