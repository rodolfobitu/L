#include "util.h"
#include "L.h"

extern void Delay1KTCYx(unsigned char unit);
extern void Delay10KTCYx(unsigned char unit);

void util_genDelay1MS(char cN) {
	/* Fcy = 12MHz => 1ms = 12kcy */
	Delay1KTCYx(12 * cN);
}

void util_genDelay10MS(char cN) {
	/* Fcy = 12MHz => 10ms = 120kcy */
	Delay10KTCYx(12 * cN);
}

void util_genDelay100MS(char cN) {
	char cI;
	for (cI = 0; cI < cN; cI++) {
		util_genDelay10MS(10);
	}
}