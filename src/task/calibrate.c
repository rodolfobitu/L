#include "L.h"
#include "pwm.h"
#include "adc.h"
#include "util.h"

/* Number of encoder steps to turn each time */
#define CALIBRATE_STEPS 3

/* PWM duty cycle for each motor */
#define CALIBRATE_LEFT_PWM 800
#define CALIBRATE_RIGHT_PWM 825

/* Output */
extern unsigned int uiSensorLimits[NUM_OF_SENSORS][2];

/* Internal */
extern unsigned int uiLeftCounter;
extern unsigned int uiRightCounter;

/*
 * The robot should be put initially aligned with the line in the ground
 * On reset, it'll make 3 moves:
 * 1) rotate clockwise `CALIBRATE_STEPS` in each wheel
 * 2) rotate counter-clockwise 2*`CALIBRATE_STEPS` in each wheel
 * 3) rotate clockwise again `CALIBRATE_STEPS` in each wheel
 * Throught the movement, we'll read each sensor to figure out the operational ranges of them
 * After this, the result will be available on `uiSensorLimits` and
 * the robot will be aligned to the line again
 */
void calibrate_run(void) {
	int i, j;
	/* 1, 2 or 3: as noted above */
	char cMoveType;
	/* Counter goal for each part of the move */
	unsigned int uiGoal;
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

	/* First move: clockwise */
	cMoveType = 1;
	pwm_setDirection(PWM_LEFT, PWM_FORWARD);
	pwm_setDutyCycle(PWM_LEFT, CALIBRATE_LEFT_PWM);
	pwm_setDirection(PWM_RIGHT, PWM_BACKWARDS);
	pwm_setDutyCycle(PWM_RIGHT, CALIBRATE_RIGHT_PWM);
	uiGoal = CALIBRATE_STEPS;
	uiLeftCounter = uiRightCounter = 0;
	LED_4 = LED_1 = LED_ON;
	
	while (1) {
		unsigned int uiValueRead;
		
		/*
		 * Read ADC values and update the ranges
		 */
		for (i = 0; i < NUM_OF_SENSORS; i++) {
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
		
		/* Turn of a wheel if it has met the goal */
		if (uiLeftCounter >= uiGoal) {
			pwm_setDutyCycle(PWM_LEFT, 0);
			LED_3 = LED_1 = LED_OFF;
		}
		if (uiRightCounter >= uiGoal) {
			pwm_setDutyCycle(PWM_RIGHT, 0);
			LED_2 = LED_4 = LED_OFF;
		}
		
		if (uiLeftCounter >= uiGoal && uiRightCounter >= uiGoal) {
			/* Next part of the move: wait 500ms and reset PWM */
			util_genDelay100MS(5);
			pwm_setDutyCycle(PWM_LEFT, CALIBRATE_LEFT_PWM);
			pwm_setDutyCycle(PWM_RIGHT, CALIBRATE_RIGHT_PWM);
			uiLeftCounter = uiRightCounter = 0;
			
			if (cMoveType == 1) {
				/* Counter clockwise */
				cMoveType = 2;
				pwm_setDirection(PWM_LEFT, PWM_BACKWARDS);
				pwm_setDirection(PWM_RIGHT, PWM_FORWARD);
				uiGoal = 2 * CALIBRATE_STEPS;
				LED_3 = LED_2 = LED_ON;
			} else if (cMoveType == 2) {
				/* Clockwise again */
				cMoveType = 3;
				pwm_setDirection(PWM_LEFT, PWM_FORWARD);
				pwm_setDirection(PWM_RIGHT, PWM_BACKWARDS);
				uiGoal = CALIBRATE_STEPS;
				LED_4 = LED_1 = LED_ON;
			} else {
				/* Done! */
				pwm_setDutyCycle(PWM_LEFT, 0);
				pwm_setDutyCycle(PWM_RIGHT, 0);
				break;
			}
		}
	}
	
	/*
	 * Export those values to global scope
	 * They'll be used by the line detection task
	 */
	for (i = 0; i < NUM_OF_SENSORS; i++) {
		uiSensorLimits[i][0] = uiMin[i][1];
		uiSensorLimits[i][1] = uiMax[i][1];
	}
}

void calibrate_runMock(void) {
	char i;
	for (i = 0; i < NUM_OF_SENSORS; i++) {
		uiSensorLimits[i][0] = 100;
		uiSensorLimits[i][1] = 500;
	}
}