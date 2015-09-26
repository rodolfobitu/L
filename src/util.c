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