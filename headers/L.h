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

#define LED_4		PORTCbits.RC7
#define LED_4_DIR	TRISCbits.RC7

#define LED_IR_ON		0
#define LED_IR_OFF		1

#define LED_IR0		PORTDbits.RD7
#define LED_IR0_DIR	TRISDbits.RD7

#define LED_IR1		PORTDbits.RD6
#define LED_IR1_DIR	TRISDbits.RD6

#define LED_IR2		PORTDbits.RD5
#define LED_IR2_DIR	TRISDbits.RD5

#define LED_IR3		PORTDbits.RD4
#define LED_IR3_DIR	TRISDbits.RD4

#define LED_IR4		PORTDbits.RD3
#define LED_IR4_DIR	TRISDbits.RD3

#define LED_IR5		PORTDbits.RD2
#define LED_IR5_DIR	TRISDbits.RD2

#endif /* L_H */