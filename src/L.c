#include "L.h"
#include "util.h"
#include "adc.h"

/* uC init configurations */

/* uC @ 48 MHz */
#pragma config FOSC   = HS
#pragma config IESO   = OFF			//Oscillator Switchover mode disabled
#pragma config PWRT   = ON			//Power-up Timer enabled
#pragma config BOR    = ON			//Brown-out Reset enabled
#pragma config BORV   = 0			//Brown-out Reset to maximum setting
#pragma config WDT    = OFF			//Watchdog timer disabled
#pragma config LVP    = OFF			//Single-Supply ICSP disabled

/* globals */
volatile unsigned int uiFlagNextPeriod = 0;	// cyclic executive flag

/* setup the interruption */
void isr_CyclicExecutive();
#pragma code high_vector=0x08
void isr_HighVector(void) {
  _asm GOTO isr_CyclicExecutive _endasm
}
#pragma code

/* setup the isr */
#pragma interrupt isr_CyclicExecutive
void isr_CyclicExecutive(void) {
	if (INTCONbits.TMR0IF) {
		/* set the cyclic executive flag */
		uiFlagNextPeriod = 1;

		/* reset the cyclic executive counting */
		util_resetCyclicExecutive();

		/* acknowledge the interrupt */
		INTCONbits.TMR0IF = 0;
	}
}

void L_init(void) {
	/* clean all ports */
	PORTA = PORTB = PORTC = PORTD = PORTE = 0;

	LED_1_DIR = OUTPUT;
	LED_2_DIR = OUTPUT;
	LED_3_DIR = OUTPUT;

	adc_init();
}

void main(void) {
	unsigned int i, adcValue;
	/* run uC init configs */
	L_init();
	
	/* config and start the cyclic executive */
	util_configCyclicExecutive();

	/* main system loop, runs forever */

	while(1) {
		/* Get 3 MSB from AN0 */
		adcValue = adc_get(5);
		LED_1 = !LED_1;
		LED_2 = adcValue >= 512 ? LED_ON : LED_OFF;
		LED_3 = adcValue >= 256 ? LED_ON : LED_OFF;

		/* WAIT FOR CYCLIC EXECUTIVE PERIOD */
		while(!uiFlagNextPeriod);
		uiFlagNextPeriod = 0;
	}
}