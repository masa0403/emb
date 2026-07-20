#include "test_plan.h"
const TestCommand TEST_PLAN[] =
{
    {CMD_DELAY,0,1000},

    {CMD_PIN_HIGH,7,0},

    {CMD_DELAY,0,100},

    {CMD_PIN_LOW,7,0},

    {CMD_END,0,0},

};
