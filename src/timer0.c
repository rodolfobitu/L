#include "L.h"

extern volatile unsigned int uiTimer0_endPeriod;
unsigned char uiResetValueHigh;
unsigned char uiResetValueLow;


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

void timer0_config(unsigned int uiTimeMs){
	/*
	FOSC = 48 MHz
	tick = 1 / (FOSC/4)
	count = time [ms] / tick
	timer = 65536 - (Count/prescale)

		OR
	timer = 65536 - (12000*t)/256
	*/
	unsigned short long uslMax = 65536,
		uslTimeMs = uiTimeMs,
		uslTime = uslMax - ((unsigned short long)12000 * uslTimeMs) / (unsigned short long)256;
	uiResetValueHigh = (uslTime >> 8) & 0xFF;
	uiResetValueLow = uslTime & 0xFF;

	T0CONbits.TMR0ON = 1; // enables TMR0
	timer0_reset();
}

unsigned int timer0_timeLeft(void) {
	/* t = 256*(65536 - timer)/12000 */
	unsigned short long uslLow = TMR0L, /* as per the datasheet, we need to read the low bits first */
		uslHigh = TMR0H,
		uslTime = uslLow + (uslHigh << 8),
		uslMax = 65536,
		uslTimeMs = ((unsigned short long)256 * (uslMax - uslTime)) / (unsigned short long)12000;
	return uslTimeMs;
}