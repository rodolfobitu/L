#include "pwm.h"
#include "L.h"

/* constant for PWM module activation */
#define PWM_MODE_MASK 	0x0C

/* duty cycle shift and maks definitions */
#define PWM_DC_SHIFT 	0x02
#define PWM_DC_MASK 	0x3FF

void pwm_init(unsigned char ucDevice) {
	/* configure PWM frequency for 46.875 kHz*/
	/* when 2 PWM are used, the frequency is the same for both */
	PR2 = 0xFF;		// TMR2 counter
	T2CON &= 0xFC;	// TMR2 prescaler configuration = 1
	
	/*
	 * Target is built to use CCP1 PWM module to
	 * activate the left motor
	 */
	if (PWM_LEFT == ucDevice) {
		/* configure initial duty cycle */
  		pwm_setDutyCycle(0, ucDevice);
	
		/* CCPxM3:CCPxM2 = 11 => PWM mode */
		CCP1CON |= PWM_MODE_MASK;
	}	
	
  	/*
	 * Target is built to use CCP2 PWM module to
	 * activate the right motor
	 */
	if (PWM_RIGHT == ucDevice) {
		/* configure initial duty cycle */
  		pwm_setDutyCycle(0, ucDevice);
	
		/* CCPxM3:CCPxM2 = 11 => PWM mode */
		CCP2CON |= PWM_MODE_MASK;
	}
	 
	/* enable TMR2 */
	T2CONbits.TMR2ON = 1;
}

/* Set duty cycle (0 - 255) */
void pwm_setDutyCycle(unsigned int uiDutyCycle, unsigned char ucDevice) {
	if(ucDevice == PWM_LEFT) {
		CCPR1L = uiDutyCycle;
 	}
 	
	if(ucDevice == PWM_RIGHT) {
		CCPR2L = uiDutyCycle;
 	}	
}