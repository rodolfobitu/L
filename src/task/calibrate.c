#include "L.h"
#include "pwm.h"
#include "adc.h"
#include "timer0.h"
#include "util.h"

extern volatile unsigned int uiTimer0_endPeriod;
extern unsigned int uiSensorLimits[NUM_OF_SENSORS][2];

void calibrate_init(void){
	int i, j;
	char cClockwise;
	/*
		We keep track of the two greatest and lowest values
		This gives us space for 1 noisy (bad) sample
		All values we get for a given sensor will be sorted as:
		{ uiMin[n][0] uiMin[n][1] ... uiMax[n][1] uiMax[n][0] }
		--- Ascending order --->
	*/
	unsigned int uiMax[NUM_OF_SENSORS][2];
	unsigned int uiMin[NUM_OF_SENSORS][2];

	/* Reset the vectors */
	for (i = 0; i < NUM_OF_SENSORS; i++) {
		for (j = 0; j < 2; j++){
			uiMin[i][j] = 1020;
			uiMax[i][j] = 0;
		}
	}

	/* Turn right for 3s */
	pwm_setDirection(PWM_LEFT, PWM_FORWARD);
	pwm_setDutyCycle(PWM_LEFT, 825);
	pwm_setDirection(PWM_RIGHT, PWM_BACKWARDS);
	pwm_setDutyCycle(PWM_RIGHT, 850);
	timer0_config(500);
	
	cClockwise = 1;
	while (1) {
		 
		unsigned int uiValueRead;
		for (i = 0; i < NUM_OF_SENSORS ; i++) {
			uiValueRead = adc_get(i);
			
			/* Save the read value if it's in the 2 extremes (as we know now) */
			if (uiMin[i][1] > uiValueRead) {
				if (uiMin[i][0] > uiValueRead) {
					uiMin[i][1] = uiMin[i][0];
					uiMin[i][0] = uiValueRead;
				} else {
					uiMin[i][1] = uiValueRead;
				}
			}
			if (uiMax[i][1] < uiValueRead) {
				if (uiMax[i][0] < uiValueRead) {
					uiMax[i][1] = uiMax[i][0];
					uiMax[i][0] = uiValueRead;
				} else {
					uiMax[i][1] = uiValueRead;
				}
			}
		}
		if (uiTimer0_endPeriod) {
			if (cClockwise) {
				cClockwise = 0;
				pwm_setDirection(PWM_LEFT, PWM_BACKWARDS);
				pwm_setDutyCycle(PWM_LEFT, 825);
				pwm_setDirection(PWM_RIGHT, PWM_FORWARD);
				pwm_setDutyCycle(PWM_RIGHT, 850);
				timer0_config(350);
			} else {
				break;
			}
		}
	}
	pwm_setDutyCycle(PWM_LEFT, 0);
	pwm_setDutyCycle(PWM_RIGHT, 0);
	/* Export those values to global scope
	 * They'll be used by the line detection task
	*/
	for (i = 0; i < NUM_OF_SENSORS; i++) {
		uiSensorLimits[i][0] = uiMin[i][1];
		uiSensorLimits[i][1] = uiMax[i][1];
	}


}
