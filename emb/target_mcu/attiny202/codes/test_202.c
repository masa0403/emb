#include <avr/io.h>

#define F_CPU 20000000UL

int main(void)
{
    /*
        PA2 : input
        PA6 : output
    */

    // PA6 output
    PORTA.DIRSET = PIN6_bm;

    // PA2 input
    PORTA.DIRCLR = PIN2_bm;


    while(1)
    {

        /*
            PA2 HIGHならPA6 HIGH
            PA2 LOWならPA6 LOW
        */

        if(PORTA.IN & PIN2_bm)
        {
            PORTA.OUTSET = PIN6_bm;
        }
        else
        {
            PORTA.OUTCLR = PIN6_bm;
        }

    }


    return 0;
}