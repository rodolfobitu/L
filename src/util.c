#include "util.h"
#include "L.h"

/*
FOSC = 20 MHz
tick = 1 / (FOSC/4)
count = time [ms] / tick
timer = 65536 - (Count/prescale)

OR
timer = 65536 - (5000/256)*t
*/

/* timer config for 3s */
#define UTIL_TIMER0_RESET_VALUE 		63583
#define UTIL_TIMER0_RESET_VALUE_HIGH    ((UTIL_TIMER0_RESET_VALUE & 0xff00) >> 8)
#define UTIL_TIMER0_RESET_VALUE_LOW 	( UTIL_TIMER0_RESET_VALUE & 0x00ff)

void util_genDelay1MS(void) {
	char i;
	for (i=0; i<69; i++) {
		Nop();
		Nop();
		Nop();
		Nop();
		Nop();
		Nop();
		Nop();
		Nop();
	}
}

void util_genDelay10MS(void) {
	char i;
	for (i=0; i<10; i++) {
		util_genDelay1MS();
	}
}

void util_genDelay100MS(void) {
	char i;
	for(i=0; i<10; i++) {
		util_genDelay10MS();
	}
}

void util_resetCyclicExecutive(void) {
	TMR0H = UTIL_TIMER0_RESET_VALUE_HIGH;
  	TMR0L = UTIL_TIMER0_RESET_VALUE_HIGH;
}

void util_configCyclicExecutive(void) {
	INTCONbits.GIE = 1;		// enables all unmasked interrupts
  	INTCONbits.PEIE = 1;	// enables all unmasked peripheral interrupts
  	INTCONbits.TMR0IE = 1; 	// enables TMR0 overflow interrup
  	
  	T0CONbits.T08BIT = 0; 	// 16-bit timer
  	T0CONbits.T0CS = 0; 	// internal clock (FOSC/4)
  	T0CONbits.PSA = 0; 		// prescaler assigned
  	T0CONbits.T0PS = 0b111; // 1:256 prescale

  	util_resetCyclicExecutive();

  	T0CONbits.TMR0ON = 1; 	// enables TMR0
}