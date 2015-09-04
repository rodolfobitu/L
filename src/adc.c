#include "adc.h"
#include "L.h"

void adc_init(void) {
	ADCON0bits.ADON = 1;
	/* Config the reference voltage */
	ADCON1bits.VCFG1 = 0; //VSS
	ADCON1bits.VCFG0 = 0; //VDD
	/* AD port configuration, for 6 channels going to ANALOG INPUT */
	ADCON1bits.PCFG = 0b1001;
	/* right justfied */
	ADCON2bits.ADFM = 1;
	/* acquistion time */
	ADCON2bits.ACQT = 0b010;  // 4 TAD
	/* converstion clock */
	ADCON2bits.ADCS = 0b101;  // 16 TOSC
}

unsigned int adc_get(char cChannel) {
	unsigned int uiLow, uiHigh;

	/* Select channel and start convertion */
	ADCON0bits.CHS = cChannel;
	ADCON0bits.GO_DONE = 1;

	/* Poll on DONE */
	while (ADCON0bits.GO_DONE);

	/* return the MSB + LSB parts */
	uiLow = ADRESL;
	uiHigh = ADRESH & 0x3;

	return (uiHigh << 8) + uiLow;
}