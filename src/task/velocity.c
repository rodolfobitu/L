#include "L.h"

#define NUMBER_OF_SAMPLES 10

static int iSamplesRight[NUMBER_OF_SAMPLES]={0};
static int iSamplesLeft[NUMBER_OF_SAMPLES] = {0};
static int iIndexRight = 0;
static int iIndexLeft = 0;
extern unsigned int uiLeftCounter;
extern unsigned int uiRightCounter;
extern unsigned int uiLeftSpeed;
extern unsigned int uiRightSpeed;


unsigned int getSpeedRight(void){
	
	int iSamplesSum = 0;
	int i;
	for (i=0; i<NUMBER_OF_SAMPLES;i++){
		iSamplesSum += iSamplesRight[i];
	}
	return (float)iSamplesSum/(float)(NUMBER_OF_SAMPLES*CYCLE_TIME);

}

unsigned int getSpeedLeft(void){

	int iSamplesSum = 0;
	int i;
	for (i=0; i<NUMBER_OF_SAMPLES;i++){
		iSamplesSum += iSamplesLeft[i];
	}
	return (float)iSamplesSum/(float)(NUMBER_OF_SAMPLES*CYCLE_TIME);

}

void velocity_task(void){

	iSamplesRight[iIndexRight++] = uiRightCounter;
	if (iIndexRight == NUMBER_OF_SAMPLES){ 
		iIndexRight = 0;
	}
	iSamplesLeft[iIndexLeft++] = uiLeftCounter;
	if (iIndexLeft == NUMBER_OF_SAMPLES){
		iIndexLeft = 0;
	}
	uiRightCounter = 0;
	uiLeftCounter = 0;

	uiLeftSpeed = getSpeedLeft();	
	uiRightSpeed = getSpeedRight();

}

