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
volatile unsigned int uiLeftCounter = 0;
volatile unsigned int uiRightCounter = 0;

unsigned int uiLeftSpeed = 0;
unsigned int uiRightSpeed = 0;

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
	
	if (INTCON3bits.INT1IF) {
		uiLeftCounter++;
		INTCON3bits.INT1IF = 0;
	}
	
	if (INTCON3bits.INT2IF) {
		uiRightCounter++;
		INTCON3bits.INT2IF = 0;
	}
}

void L_init(void) {
	/* clean all ports */
	PORTA = PORTB = PORTC = PORTD = PORTE = 0;

	LED_1_DIR = OUTPUT;
	LED_2_DIR = OUTPUT;
	LED_3_DIR = OUTPUT;
	LED_4_DIR = OUTPUT;

	LED_IR0_DIR = OUTPUT;
	LED_IR1_DIR = OUTPUT;
	LED_IR2_DIR = OUTPUT;
	LED_IR3_DIR = OUTPUT;
	LED_IR4_DIR = OUTPUT;
	LED_IR5_DIR = OUTPUT;

	/* set up interruption bits */
	INTCON3bits.INT1IE = 1;
	INTCON3bits.INT2IE = 1;

	adc_init();
}

/* Read speed counter, save it and reset it */
void task_getSpeed(void) {
	uiLeftSpeed = uiLeftCounter;
	uiRightSpeed = uiRightCounter;
	uiLeftCounter = 0;
	uiRightCounter = 0;
}

void main(void) {
	unsigned int i, adcValue;
	
	/* run uC init configs */
	L_init();

	/* Turn all IR leds on */
	
	/* config and start the cyclic executive */
	util_configCyclicExecutive();

	/* main system loop, runs forever */

	while(1) {
		task_getSpeed();

		/* Set IR leds */		
		LED_IR0 = LED_IR_ON;
		LED_IR1 = LED_IR2 = LED_IR3 = LED_IR4 = LED_IR5 = LED_IR_OFF;

		/* Read from analog input */
		adcValue = adc_get(0);

		/* Show result */
		LED_4 = (adcValue >> 9) & 0x1;
		LED_1 = (adcValue >> 8) & 0x1;
		LED_2 = (adcValue >> 7) & 0x1;
		LED_3 = (adcValue >> 6) & 0x1;

		/* Wait for period */
		while(!uiFlagNextPeriod);
		uiFlagNextPeriod = 0;
	}
}