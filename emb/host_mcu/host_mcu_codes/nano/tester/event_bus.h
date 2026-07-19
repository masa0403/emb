#ifndef EVENT_BUS_H
#define EVENT_BUS_H

#include "event.h"

typedef void (*EventCallback)(const PinEvent&);

class EventBus
{
public:

    void begin();

    void subscribe(EventCallback callback);

    void publish(const PinEvent& event);

private:

    static constexpr uint8_t MAX_SUBSCRIBERS = 4;

    EventCallback callbacks[MAX_SUBSCRIBERS];

    uint8_t callbackCount = 0;
};

extern EventBus eventBus;

#endif