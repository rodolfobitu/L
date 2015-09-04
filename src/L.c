#include "L.h"

/* uC init configurations */

/* uC @ 48 MHz */
#pragma config PLLDIV = 1 			//Divide by 1 (04 MHz oscillator input)
#pragma config CPUDIV = OSC1_PLL2 	//96 MHz PLL Src: /2
#pragma config FOSC   = XTPLL_XT	//XT oscillator, PLL enabled
#pragma config IESO   = OFF			//Oscillator Switchover mode disabled
#pragma config PWRT   = ON			//Power-up Timer enabled
#pragma config BOR    = ON			//Brown-out Reset enabled
#pragma config BORV   = 0			//Brown-out Reset to maximum setting
#pragma config WDT    = OFF			//Watchdog timer disabled
#pragma config LVP    = OFF			//Single-Supply ICSP disabled

void L_init(void) {
	/* clean all ports */
	PORTA = PORTB = PORTC = PORTD = PORTE = 0;

	LED_1_DIR = OUTPUT;
	LED_2_DIR = OUTPUT;
	LED_3_DIR = OUTPUT;
}

void main(void) {
	/* run uC init configs */
	L_init();

	/* main system loop, runs forever */
	while(1) {
		LED_1 = LED_ON;
		LED_2 = LED_OFF;
	}
}