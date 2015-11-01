#include "L.h"
#include "pwm.h"
#include "util.h"

extern volatile unsigned int uiLeftCounter;
extern volatile unsigned int uiRightCounter;

/**
 * Test the given side for the static and dynamic minimun PWM value
 * The results will be outputed in integer pointers provided
 */
static void minPwm_test(unsigned char ucSide, int *piStatic, int *piDynamic, volatile unsigned int *puiCounter) {
	char cBit;
	
	/* Avoid any initial predisposition by setting the target side to maximum */
	pwm_setDirection(ucSide, PWM_FORWARD);
	pwm_setDutyCycle(ucSide, 1023);
	util_genDelay100MS(10);
	pwm_setDutyCycle(ucSide, 0);
	util_genDelay100MS(10);
	
	/*
	 * Static test: guess each bit, from MSB to LSB
	 */
	*piStatic = 0;
	for (cBit = 9; cBit >= 0; cBit--) {
		/* Prepare guess */
		int iGuessStep = (int)1 << cBit;
		*piStatic += iGuessStep;
		
		/* Apply it */
		pwm_setDutyCycle(ucSide, 0);
		util_genDelay100MS(5);
		*puiCounter = 0;
		pwm_setDutyCycle(ucSide, *piStatic);
		LED_2 = LED_ON;
		util_genDelay100MS(5);
		LED_2 = LED_OFF;
		
		/* If motor has moved, the guess was too big */
		if (*puiCounter) {
			*piStatic -= iGuessStep;
			LED_4 = LED_ON;
		} else {
			LED_4 = LED_OFF;
		}
	}
	
	/*
	 * Dynamic test: guess each bit, from MSB to LSB
	 */
	*piDynamic = 0;
	for (cBit = 9; cBit >= 0; cBit--) {
		/* Prepare guess */
		int iGuessStep = (int)1 << cBit;
		*piDynamic += iGuessStep;
		
		/* Apply it */
		pwm_setDutyCycle(ucSide, 1023);
		util_genDelay100MS(5);
		pwm_setDutyCycle(ucSide, *piDynamic);
		util_genDelay100MS(5);
		*puiCounter = 0;
		LED_2 = LED_ON;
		util_genDelay100MS(5);
		LED_2 = LED_OFF;
		
		/* If motor has moved, the guess was too big */
		if (*puiCounter) {
			*piDynamic -= iGuessStep;
			LED_4 = LED_ON;
		} else {
			LED_4 = LED_OFF;
		}
	}

	/* Finish */
	pwm_setDutyCycle(ucSide, 0);
}

/**
 * Show a 10-bit result in the 4 leds, like this:
 * 1) turn on all leds
 * 2) show 4 MSBs (the MSB in the red led)
 * 3) show next 4 MSBs (the MSB in the red led)
 * 4) show 2 LSBs (the MSB in the red led)
 */
static void minPwm_showResult(int iValue) {
	LED_3 = LED_2 = LED_1 = LED_4 = LED_ON;
	util_genDelay100MS(5);
	
	LED_4 = (iValue >> 9) & 1;
	LED_1 = (iValue >> 8) & 1;
	LED_2 = (iValue >> 7) & 1;
	LED_3 = (iValue >> 6) & 1;
	util_genDelay100MS(5);
	
	LED_4 = (iValue >> 5) & 1;
	LED_1 = (iValue >> 4) & 1;
	LED_2 = (iValue >> 3) & 1;
	LED_3 = (iValue >> 2) & 1;
	util_genDelay100MS(5);
	
	LED_4 = (iValue >> 1) & 1;
	LED_1 = iValue & 1;
	LED_2 = LED_OFF;
	LED_3 = LED_OFF;
	util_genDelay100MS(5);
}

void minPwm_run(void) {
	int iStaticRight, iDynamicRight, iStaticLeft, iDynamicLeft;
	
	/* Test each side */
	LED_3 = LED_ON;
	minPwm_test(PWM_LEFT, &iStaticLeft, &iDynamicLeft, &uiLeftCounter);
	LED_3 = LED_OFF;
	LED_1 = LED_ON;
	minPwm_test(PWM_RIGHT, &iStaticRight, &iDynamicRight, &uiRightCounter);
	LED_1 = LED_OFF;
	
	/* Show results */
	while (1) {
		minPwm_showResult(iStaticLeft);
		minPwm_showResult(iDynamicLeft);
		minPwm_showResult(iStaticRight);
		minPwm_showResult(iDynamicRight);
		LED_3 = LED_2 = LED_1 = LED_4 = LED_OFF;
		util_genDelay100MS(5);
	}
}