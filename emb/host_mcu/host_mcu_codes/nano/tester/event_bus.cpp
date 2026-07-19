#include "event_bus.h"

EventBus eventBus;

void EventBus::begin()
{
    callbackCount = 0;
}

void EventBus::subscribe(EventCallback callback)
{
    if(callbackCount >= MAX_SUBSCRIBERS)
        return;

    callbacks[callbackCount++] = callback;
}

void EventBus::publish(const PinEvent& event)
{
    for(uint8_t i=0;i<callbackCount;i++)
    {
        callbacks[i](event);
    }
}