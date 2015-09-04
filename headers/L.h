#ifndef L_H
#define L_H

/* uC registers definition */
#include <p18F4550.h>

/* port directions */
#define INPUT			1
#define OUTPUT			0

/* LEDs definition */
#define LED_ON		1
#define LED_OFF		0

#define LED_1		PORTDbits.RD0
#define LED_1_DIR	TRISDbits.RD0

#define LED_2		PORTDbits.RD1
#define LED_2_DIR	TRISDbits.RD1

#define LED_3		PORTCbits.RC6
#define LED_3_DIR	TRISCbits.RC6

#endif /* L_H */