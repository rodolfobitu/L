#include "util.h"
#include "L.h"

void util_genDelay1MS(void) {
	int i;
	for (i=0; i<1000; i++) {
		Nop();
		Nop();
		Nop();
		Nop();
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

void util_genDelay10MS(char cN) {
	int i, cMax = 10*cN;
	for(i = 0; i < cMax; i++) {
		util_genDelay1MS();
	}
}

void util_genDelay100MS(char cN) {
	int i, cMax = 10*cN;
	for(i = 0; i < cMax; i++) {
		util_genDelay10MS(1);
	}
}