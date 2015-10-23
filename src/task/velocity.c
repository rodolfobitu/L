#include "L.h"

#define VELOCITY_NUM_SAMPLES 3

/* Output data */
extern float fLeftSpeed;
extern float fRightSpeed;

/* Internal usage */
extern unsigned int uiLeftCounter;
extern unsigned int uiRightCounter;
static int iSamplesRight[VELOCITY_NUM_SAMPLES] = {0};
static int iSamplesLeft[VELOCITY_NUM_SAMPLES] = {0};
static int iIndex = 0;

float velocity_calcSpeed(int iSamples[]) {
	int iSamplesSum = 0;
	int i;
	for (i=0; i<VELOCITY_NUM_SAMPLES; i++) {
		iSamplesSum += iSamples[i];
	}
	return (float)iSamplesSum / (float)(VELOCITY_NUM_SAMPLES * CYCLE_TIME);
}

void velocity_task(void) {
	iSamplesLeft[iIndex] = uiLeftCounter;
	iSamplesRight[iIndex] = uiRightCounter;
	iIndex++;
	if (iIndex == VELOCITY_NUM_SAMPLES){ 
		iIndex = 0;
	}
	uiRightCounter = 0;
	uiLeftCounter = 0;

	fLeftSpeed = velocity_calcSpeed(iSamplesLeft);
	fRightSpeed = velocity_calcSpeed(iSamplesRight);
}