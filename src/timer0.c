#include "L.h"

extern volatile unsigned int uiTimer0_endPeriod;
unsigned int uiResetValueHigh;
unsigned int uiResetValueLow;


void timer0_init(void) {
	INTCONbits.TMR0IE = 1; 	// enables TMR0 overflow interrup

	T0CONbits.T08BIT = 0; 	// 16-bit timer
	T0CONbits.T0CS = 0; 	// internal clock (FOSC/4)
	T0CONbits.PSA = 0; 		// prescaler assigned
	T0CONbits.T0PS = 0b111; // 1:256 prescale
}

void timer0_reset(void) {
	TMR0H = uiResetValueHigh;
	TMR0L = uiResetValueLow;
	uiTimer0_endPeriod = 0;
}

void timer0_config(unsigned short long uslTimeMs){
	/*
	FOSC = 48 MHz
	tick = 1 / (FOSC/4)
	count = time [ms] / tick
	timer = 65536 - (Count/prescale)

		OR
	timer = 65536 - (12000/256)*t
	*/

	unsigned short long uslTime = (unsigned short long)65536 - ((unsigned short long)12000*uslTimeMs/(unsigned short long)256);
	uiResetValueHigh = ((uslTime & 0xff00) >> 8);
	uiResetValueLow =  (uslTime & 0x00ff);

	T0CONbits.TMR0ON = 1; 	// enables TMR0
	timer0_reset();
}